FROM mysql:latest

# Set environment variables for the new user
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=test
ENV MYSQL_DATABASE=site

COPY ./scripts /docker-entrypoint-initdb.d/
