from setuptools import setup

setup(
    name='flask_app',
    packages=['department_app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
