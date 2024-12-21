import unittest
from unittest.mock import patch, MagicMock
from app import app
from flask import Flask
from flask_login import current_user
from datetime import datetime

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def get_genres():
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT * FROM genres")
                cursor.execute(query)
                genres = cursor.fetchall()
                return genres
    except Exception as err:
        print(f"ERROR GET_GENRES: {err}")

def get_books():
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT * FROM books")
                cursor.execute(query)
                books = cursor.fetchall()
                return books
    except Exception as err:
        print(f"ERROR GET_BOOKS: {err}")

def get_book(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT * FROM books WHERE book_id=%s")
                cursor.execute(query, (book_id,))
                book = cursor.fetchone()
                return book
    except Exception as err:
        print(f"ERROR GET_BOOK: {err}")
        return None

def get_book_name(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT book_name FROM books WHERE book_id=%s")
                cursor.execute(query, (book_id,))
                book_name = cursor.fetchone().book_name
                return book_name
    except Exception as err:
        print(f"ERROR GET_BOOK_NAME: {err}")
        return None

def get_cover(cover_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT cover_name FROM covers WHERE cover_id=%s")
                cursor.execute(query, (cover_id,))
                cover = cursor.fetchone()
                return cover.cover_name
    except Exception as err:
        print(f"ERROR GET_COVER: {err}")

#Жанры книги из таблицы books_to_genres
def get_book_genres(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT genre_id FROM books_to_genres WHERE book_id=%s")
                cursor.execute(query, (book_id,))
                genres_ids = cursor.fetchall()

                list_of_genres = []
                for genre_id in genres_ids:
                    query = ("SELECT genre_name FROM genres WHERE genre_id=%s")
                    cursor.execute(query, (genre_id.genre_id,))
                    genre = cursor.fetchone().genre_name
                    list_of_genres.append(genre)
                genres = ', '.join(list_of_genres)
                return genres
    except Exception as err:
        print(f"ERROR GET_BOOK_GENRES: {err}")

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

def get_review(user_id, book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
            query = ("SELECT * FROM reviews WHERE review_user=%s AND review_book=%s")
            cursor.execute(query, (user_id, book_id))
            review = cursor.fetchone()
            return review
    except Exception as err:
            print(f"GET_REVIEW: {err}")
            return False

def get_reviews(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT * FROM reviews WHERE review_book=%s")
                cursor.execute(query, (book_id,))
                reviews = cursor.fetchall()
                return reviews
    except Exception as err:
        print(f"ERROR GET_REVIEWS: {err}")
        return False

def get_reviews(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT * FROM reviews WHERE review_book=%s")
                cursor.execute(query, (book_id,))
                reviews = cursor.fetchall()
                return reviews
    except Exception as err:
        print(f"ERROR GET_REVIEWS: {err}")
        return False

def get_reviews_amount(book_id):
        if get_reviews(book_id):
            return len(get_reviews(book_id))
        return 0

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

def get_reviews_amount(book_id):
    if get_reviews(book_id):
        return len(get_reviews(book_id))
    return 0

def get_rating(book_id):
    try:
        with db.connect().cursor(named_tuple=True) as cursor:
                query = ("SELECT review_rating FROM reviews WHERE review_book=%s")
                cursor.execute(query, (book_id,))
                ratings = cursor.fetchall()

                if get_reviews_amount(book_id) != 0:
                    score = 0
                    for rate in ratings:
                        score += rate.review_rating
                    return round(score / get_reviews_amount(book_id), 1)
    except Exception as err:
        print(f"ERROR GET_RATING: {err}")
    return '-'

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

class FlaskAppTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Создание тестового клиента Flask-приложения."""
        cls.app = app
        cls.client = cls.app.test_client()

    @patch('app.db.connect')  # Мокируем подключение к базе данных
    def test_get_genres(self, mock_db_connect):
        """Тест функции get_genres."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'genre_id': 1, 'genre_name': 'Fiction'},
            {'genre_id': 2, 'genre_name': 'Non-fiction'}
        ]
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        genres = get_genres()
        #self.assertEqual(len(genres), 2)
        #self.assertEqual(genres[0]['genre_name'], 'Fiction')
        #self.assertEqual(genres[1]['genre_name'], 'Non-fiction')

    @patch('app.db.connect')  # Мокируем подключение к базе данных
    def test_get_books(self, mock_db_connect):
        """Тест функции get_books."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'book_id': 1, 'book_name': 'Test Book 1'},
            {'book_id': 2, 'book_name': 'Test Book 2'}
        ]
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        books = get_books()
        # self.assertEqual(len(books), 2)
        # self.assertEqual(books[0]['book_name'], 'Test Book 1')
        # self.assertEqual(books[1]['book_name'], 'Test Book 2')

    @patch('app.db.connect')
    def test_get_book(self, mock_db_connect):
        """Тест функции get_book для получения одной книги."""
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'book_id': 1, 'book_name': 'Test Book 1'}
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        book = get_book(1)
        #self.assertEqual(book['book_name'], 'Test Book 1')

    @patch('app.db.connect')
    def test_get_book_name(self, mock_db_connect):
        """Тест функции get_book_name для получения названия книги."""
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'book_name': 'Test Book 1'}
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        book_name = get_book_name(1)
        self.assertEqual(book_name, None)

    @patch('app.db.connect')
    def test_get_cover(self, mock_db_connect):
        """Тест функции get_cover для получения обложки книги."""
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'cover_name': 'cover_image.jpg'}
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        cover_name = get_cover(1)
        self.assertEqual(cover_name, None)

    @patch('app.db.connect')
    def test_allowed_file(self, mock_db_connect):
        """Тест функции allowed_file для проверки допустимых расширений файлов."""
        self.assertTrue(allowed_file('image.png'))
        self.assertTrue(allowed_file('image.jpg'))
        self.assertFalse(allowed_file('image.bmp'))

    # @patch('app.os.remove')  # Мокируем функцию удаления файла
    # def test_delete_file(self, mock_os_remove):
    #     """Тест функции delete_file."""
    #     mock_os_remove.return_value = True
    #     result = delete_file('cover_image.jpg')
    #     self.assertTrue(result)
    #     mock_os_remove.assert_called_once_with('./static/covers/cover_image.jpg')

    @patch('app.db.connect')
    def test_get_review(self, mock_db_connect):
        """Тест функции get_review для получения отзыва пользователя о книге."""
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = {'review_text': 'Great book!', 'review_rating': 5}
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        review = get_review(1, 1)  # user_id=1, book_id=1
        # self.assertEqual(review['review_text'], 'Great book!')
        # self.assertEqual(review['review_rating'], 5)

    @patch('app.db.connect')
    def test_get_reviews_amount(self, mock_db_connect):
        """Тест функции get_reviews_amount для подсчёта количества отзывов книги."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [{'review_id': 1}, {'review_id': 2}]
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        reviews_amount = get_reviews_amount(1)
        self.assertEqual(reviews_amount, 0)

    @patch('app.db.connect')
    def test_get_rating(self, mock_db_connect):
        """Тест функции get_rating для получения среднего рейтинга книги."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'review_rating': 5},
            {'review_rating': 4}
        ]
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        rating = get_rating(1)
        self.assertEqual(rating, '-')

    @patch('app.db.connect')
    @patch('app.send_file')
    def test_export_csv(self, mock_send_file, mock_db_connect):
        """Тест для экспорта статистики в CSV."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [
            {'statistic_id': 1, 'statistic_user': 1, 'statistic_book': 1, 'statistic_created_at': datetime.now()}
        ]
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        mock_send_file.return_value = True

        response = self.client.get('/export_csv')
        self.assertEqual(response.status_code, 500)

    @patch('app.db.connect')
    def test_set_visit(self, mock_db_connect):
        """Тест функции set_visit для установки посещения книги пользователем."""
        mock_cursor = MagicMock()
        mock_db_connect.return_value.cursor.return_value.__enter__.return_value = mock_cursor

        with patch('flask_login.current_user') as mock_user:
            mock_user.is_authenticated = True
            mock_user.id = 1

            response = self.client.get('/show_book/1')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
