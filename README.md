# Shoe sales website 

## This project is a website for selling shoes, with ***user management***.

This project was made in Python v3.12.2 using Django framework v5.0.3 and Bootstrap framework v5.0.
It includes:
- CRUDs
- User management with middleware
- Data validation for ensuring accuracy
- Migrations and Seeders Management

## Installation requirements
- Python 3.x.y (https://www.python.org/downloads/)
- Django 5.x (https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release)
- A database system like MySQL

## Installation
```bash
# Clone this repository
$ git clone https://github.com/erwanngat/LaravelShoe

# Go into the repository
$ cd djangowin

# Set up the settings file in the djangoWin directory with your secret key and database information
# You can generate you secrete key like this
$ py manage.py shell
$ from django.core.management.utils import get_random_secret_key
$ print(get_random_secret_key())
# You can copy and paste the new secret key

# Migrate the database
$ py manage.py migrate

# Start your local server 
$ py manage.py runserver

# Access the website
In your browser, type http://localhost:8000

# Accounts
You can create a normal account by just complete the register form

To get access to the admin you can create a superuser like this :
$ py manage.py createsuperuser
and type http://localhost:8000/admin

```

## License 

Code Licensed Under [GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) | Content Under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
