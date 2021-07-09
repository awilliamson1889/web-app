[![build](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml/badge.svg)](https://github.com/awilliamson1889/web-app/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/awilliamson1889/web-app/badge.svg?branch=create-code-quality)](https://coveralls.io/github/awilliamson1889/web-app?branch=create-code-quality)

# Web-app

# Create and run migrations


```{bash}
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
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
