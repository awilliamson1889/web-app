from setuptools import setup

setup(
    name='web-app',
    package=['department_app'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
