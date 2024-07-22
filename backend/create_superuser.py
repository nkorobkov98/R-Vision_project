import os
import django
from dotenv import load_dotenv


load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  

# Инициализация Django
django.setup()

def create_superuser():
    from django.contrib.auth.models import User
    username = os.getenv('DJANGO_SUPERUSER_USERNAME')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f'Superuser "{username}" created.')
    else:
        print(f'Superuser "{username}" already exists. Skipping creation.')

if __name__ == "__main__":
    create_superuser()

