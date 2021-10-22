
FROM ubuntu:latest
FROM python

COPY . .

EXPOSE 8000

RUN apt-get update -y

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "department_app.wsgi:app"]