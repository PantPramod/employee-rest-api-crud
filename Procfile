web: gunicorn employeeApp.wsgi
release: python manage.py makemigrations 
release: python manage.py collectstatic 
release: python manage.py migrate 