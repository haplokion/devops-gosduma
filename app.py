import os, io

from datetime import date

from flask import (
    Flask,
    render_template,
    flash,
    request,
    redirect,
    url_for,
    session,
    send_file
)
from flask_login import login_required, current_user

UPLOAD_FOLDER = "./static/covers"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

from database import Database
db = Database(app)

from auth import bp as bp_auth, init_login_manager, checkRole
app.register_blueprint(bp_auth)
init_login_manager(app)

#Проверка расширения файла
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#Сохранение файла
def save_file(file, filename):
    try:
        file.stream.seek(0)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return True
    except Exception as err:
        print(f"ERROR SAVE_FILE: {err}")
        return False

#Удаление файла
def delete_file(filename):
    try:
        path_file = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        os.remove(path_file)
        return True
    except Exception:
        return False

def get_login(user_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
            query = ("SELECT user_login FROM users WHERE user_id=%s")
            cursor.execute(query, (user_id,))
            login = cursor.fetchone()
            return login.user_login
    except Exception as err:
            print(f"GET_LOGIN: {err}")
            return False

def set_visit(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
            if current_user.is_authenticated:
                user_id = current_user.id

                query = ("INSERT INTO statistics(statistic_user, statistic_book) VALUES (%s, %s)")
                cursor.execute(query, (user_id, book_id))
            else:
                query = ("INSERT INTO statistics(statistic_book) VALUES (%s)")
                cursor.execute(query, (book_id,))
            db.connect().commit()
    except Exception as err:
        db.connect().rollback()
        print(f"ERROR SET_VISIT: {err}")
    return ''

def get_fio(user_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
            query = ("SELECT * FROM users WHERE user_id=%s")
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            fio = user.user_surname + ' ' + user.user_name + ' ' + user.user_patronym
            return fio
    except Exception as err:
            print(f"GET_FIO: {err}")
            return "Неаутентифицированный пользователь"

@app.route("/export_csv")
def export_csv():
    with db.connect().cursor(named_tuple=True) as cursor:
        query = ('SELECT * FROM statistics')
        cursor.execute(query)
        statistics=cursor.fetchall()

        statistic=[]
        for i in statistics:
            string = {"id": i.statistic_id, "ФИО": get_fio(i.statistic_user), "Время посещения": i.statistic_created_at}
            statistic.append(string)

        print(statistic)
        data = load_data(statistic, ["id", "ФИО", "Время посещения"])
        download_name = "Статистика_" + str(date.today()) + ".csv"
        return send_file(data, as_attachment=True, download_name=download_name)

def load_data(records, fields):
    csv_data=", ".join(fields)+"\n"
    for record in records:
        csv_data += ", ".join([str(record[field]) for field in fields]) + "\n"
    print(csv_data)
    f = io.BytesIO()
    f.write(csv_data.encode("utf-8"))
    f.seek(0)
    return f

@app.route("/")
def index():
    return render_template("app.html")

@app.route('/delete_user/<int:user_id>')
@login_required
@checkRole("delete")
def delete_user(user_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("DELETE FROM users WHERE user_id=%s")
                cursor.execute(query, (user_id,))
                db.connect().commit()
                flash("Удаление успешно", "success")
    except Exception as err:
        flash("Ошибка при удалении пользователя", "danger")
        db.connect().rollback()
        print(f"ERROR DELETE_USER: {err}")
    return redirect(url_for("index"))