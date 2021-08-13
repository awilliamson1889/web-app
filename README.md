[![build](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml/badge.svg)](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/awilliamson1889/web-app/badge.svg?branch=create-db)](https://coveralls.io/github/awilliamson1889/web-app?branch=create-db)

# Web-app
# Install dependencies
```{bash}
pip install -r requirements.txt
```
# Create database
```{bash}
$ sudo apt install postgresql
$ sudo -i -u postgres
$ psql
postgres=# CREATE USER jacky WITH PASSWORD 
'mystrongpassword';
postgres=# CREATE DATABASE gallery;
postgres=# GRANT ALL PRIVILEGES ON DATABASE gallery to jacky;
postgres=# \q
$ exit
```

# Create and run migrations


```{bash}
$ export FLASK_APP=department_app.app
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```
# Create .env file
department_app/.env
```{bash}
SECRET_KEY='veryveryswcretkey'
DB_USER_NAME='jacky'
DB_PASSWORD='mystrongpassword'
DB_NAME='gallery'
DB_DRIVER='postgresql'
DB_HOST='localhost'
DB_PORT='5432'
```

# Run

```{bash}
gunicorn --bind 127.0.0.1:5000 department_app.wsgi:app
```

Open http://127.0.0.1:5000 in a browser.
