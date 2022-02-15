web: gunicorn employeeAPIProject.wsgi
release: python manage.py makemigrations --employeeApp
release: python manage.py collectstatic --noinput
release: python manage.py migrate --employeeApp