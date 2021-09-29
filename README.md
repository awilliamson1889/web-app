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
# Flask Migrate
```{bash}
$ export FLASK_APP=department_app.app
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
```

# Create ENV variables
```{bash}
export APP_SETTINGS=department_app.config.ProductionConfig

also you can chose TestingConfig for tests
export APP_SETTINGS=department_app.config.TestingConfig

or DevelopmentConfig for development
export APP_SETTINGS=department_app.config.DevelopmentConfig


export SECRET_KEY='veryveryswcretkey'
export DB_USER_NAME='jacky'
export DB_PASSWORD='mystrongpassword'
export DB_NAME='gallery'
export DB_DRIVER='postgresql'
export DB_HOST='localhost'
export DB_PORT='5432'
```

# Run

```{bash}
gunicorn --bind 127.0.0.1:5000 department_app.wsgi:app
```

Open http://127.0.0.1:5000/swagger/ or  http://127.0.0.1:5000/employee/1 in a browser.
