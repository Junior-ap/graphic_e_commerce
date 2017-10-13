import os
os.system("python manage.py makemigrations products accounts address store categories")
os.system("python manage.py migrate")
# os.system("python3 manage.py runserver")
