# Agroforestry Management System
Overview
The Agroforestry Management System is a web application designed to manage farmer data and facilitate 
efficient agroforestry practices. This application allows users to add, edit, and manage farmer information,
 including contact details, plot locations, tree species, and field photos. The goal is to provide an organized 
 and user-friendly interface for both field executives and managers in the agroforestry sector.


Features
User authentication (login and logout)
Admin panel for managing farmer data
Add, edit, and delete farmer information
Upload and display field photos

 ## Technologies Used

- Python
- Django (Backend framework)
- HTML/CSS (Frontend)
- SQLite (Database)

Credentials
Admin User:

Username: sejal
Password: sejal2001# 
Regular User:

Username: A (Exicutive A)
Password: password123 
Username: B (Exicutive B)
Password: password123 
Username: C (Manager C)
Password: password123 
Username: D (Manager D)
Password: password123 
Username: E (Manager E)
Password: password123 

Installation
Clone the Repository:

bash

git clone https://github.com/sejal1234desai/agroforestry_management_system.git

Navigate to the Project Directory:
cd agroforestry_management_system

bash
pip install -r requirements.txt

Run Migrations:
pip install -r requirements.txt

Create a Superuser (Admin):
python manage.py createsuperuser
Follow the prompts to set up your admin account.

Run the Development Server:

python manage.py runserver
Access the Application: Open your browser and go to http://127.0.0.1:8000/.

Credentials
Admin User:

Username: admin
Password: admin_password 
Regular User:

Username: user
Password: user_password (Change this according to your preference)
Usage
After logging in, users can manage farmer data through the admin panel. Users with appropriate permissions can add, edit, and delete farmers, view existing records, and upload field photos.

If you want to automate user creation during setup:

Use a custom Django management command or a script to create these users and assign roles programmatically.
from django.contrib.auth.models import User
from farmers.models import TeamMember

def create_users():
    users = [
        {'username': 'A', 'role': 'Field Executive'},
        {'username': 'B', 'role': 'Field Executive'},
        {'username': 'C', 'role': 'Field Manager'},
        {'username': 'D', 'role': 'Field Manager'},
        {'username': 'E', 'role': 'Senior Manager'},
    ]

    for user_data in users:
        user, created = User.objects.get_or_create(username=user_data['username'])
        user.set_password('password123')  # Set a default password
        user.save()
        TeamMember.objects.get_or_create(user=user, role=user_data['role'])

create_users()


##Run this script in the Django shell (python manage.py shell).




**
