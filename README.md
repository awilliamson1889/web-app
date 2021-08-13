[![build](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml/badge.svg)](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/awilliamson1889/web-app/badge.svg?branch=create-db)](https://coveralls.io/github/awilliamson1889/web-app?branch=create-db)

# Web-app

# Create database
```{bash}
$ sudo apt install postgresql
$ sudo -i -u postgres
$ psql
postgres=# CREATE USER jacky WITH PASSWORD 
'mystrongpassword';
postgres=# CREATE DATABASE gallery;
postgres=# GRANT ALL PRIVILEGES ON DATABASE gallery to jacky;
postgres=# q
```

# Create and run migrations


```{bash}
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```
# Create .env file
web-app/.env
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
$ export FLASK_APP=department_app
$ export FLASK_ENV=development
$ flask run
```
Or on Windows cmd:
```{bash}
> set FLASK_APP=department_app
> set FLASK_ENV=development
> flask run
```
Open http://127.0.0.1:5000 in a browser.
