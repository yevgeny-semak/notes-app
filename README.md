# Notes App
To run this project
1. clone repository to your local directory\
`git clone https://github.com/yevgenysemak/notes-app.git`
2. install dependencies from pipenv\
`cd notes-app`\
`mkdir .venv`\
`pipenv install`
3. run venv\
`pipenv shell`
4. create .env file in project directory
`touch .env`
6. fill in all environment variables in .env file according to .env.template file.\
8. make sure you have postgresql database set and running\
9. run migrations to database\
`python3 manage.py makemigrations`\
`python3 manage.py migrate`
6. create superuser\
`python3 manage.py createsuperuser`
7. run server\
`python3 manage.py runserver `
8. navigate to\
`127.0.0.1:8000`
