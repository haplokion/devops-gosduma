FROM python:3.11-alpine

# Create and set the working directory
WORKDIR /app

# Copy only the requirements file first to leverage Docker caching
# COPY requirements.txt .

# COPY requirements and application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN echo "superpassword123" > password.txt
RUN rm -rf password.txt

# Copy the entire application code
# COPY . .

# Expose the port your application will run on
EXPOSE 5000
EXPOSE 3306

# Specify the command to run on container start
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
