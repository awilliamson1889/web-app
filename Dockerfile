
FROM ubuntu:latest
FROM python

COPY . .

EXPOSE 8000

RUN apt-get update -y

RUN pip install -r requirements.txt

ENV FLASK_APP="department_app.app"
ENV APP_SETTINGS="department_app.config.ProductionConfig"

ENV SECRET_KEY="veryveryswcretkey"
ENV DB_USER_NAME="jacky"
ENV DB_PASSWORD="mystrongpassword"
ENV DB_NAME="gallery"
ENV DB_DRIVER="postgresql"
# ENV DB_HOST="172.18.0.1"
ENV DB_PORT="5432"

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "department_app.wsgi:app"]