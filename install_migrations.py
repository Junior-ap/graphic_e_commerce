import os
os.system("python manage.py makemigrations products accounts")
os.system("python manage.py migrate")
# os.system("python3 manage.py runserver")
