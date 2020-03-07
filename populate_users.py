import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstDjangoProject.settings')

import django
django.setup()

from first_app.models import User
from faker import Faker

fake_user = Faker()

def populate_user(n=5):
    for i in range(n):
        fake_fname = fake_user.first_name()
        fake_lname = fake_user.last_name()
        fake_email = fake_user.email()

        usr = User.objects.get_or_create(FirstName=fake_fname,LastName=fake_lname,Email=fake_email)[0]

if __name__ == '__main__':
    print("populating Script")
    populate_user(10)
    print("populating complete!")