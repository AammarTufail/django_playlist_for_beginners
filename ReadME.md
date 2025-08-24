# Django Playlist for Beginners in Urdu

This repository is part of the following playlist on DJANGO for Beginners in Urdu.

> The playlist link is [here](https://www.youtube.com/watch?v=KA8GLE8YPGs&list=PL9XvIvvVL50GrR46L_U_eKQHab-BKsvDm&ab_channel=Codanics). 
--- 
> Or you can also access by clicking on the image below.

[![Django for Beginners in Urdu](https://img.youtube.com/vi/KA8GLE8YPGs/0.jpg)](https://www.youtube.com/watch?v=KA8GLE8YPGs&list=PL9XvIvvVL50GrR46L_U_eKQHab-BKsvDm&ab_channel=Codanics)


## 1. Installation

### 1.1. Install python, gitbash and miniconda
- Python can be installed from here: [python.org](https://www.python.org/downloads/).
- Git Bash can be installed from here: [git-scm.com](https://git-scm.com/downloads).
- If you want to use miniconda, you can install it from here: [miniconda](https://docs.conda.io/en/latest/miniconda.html).


### 1.2. create a virtual environment and install django

This creates a virtual environment for your Django project.

```bash
python -m venv .venv
source .venv/bin/activate # for Linux/Mac
# gitbash and venv in windows
source .venv/Scripts/activate
.venv\Scripts\activate # for Windows
pip install django
```

## 2. Create a Django project

```bash
django-admin startproject codanics
```

## 3. Run django development server

```bash
# without mentioning any port
python manage.py runserver
# or
# with a port number
python manage.py runserver 8001
```

## 4. Create an app

Apps in django are modular components that encapsulate specific functionality. They can be reused across different projects.

```bash
python manage.py startapp courses
```

# What each files shows in project

- `manage.py`: A command-line utility that lets you interact with this Django project in various ways.
  - Example:
    - `python manage.py migrate`: Applies database migrations.
    - `python manage.py runserver`: Starts the development server.
    - `python manage.py createsuperuser`: Creates a superuser account.
    - `python manage.py makemigrations`: Creates new migrations based on the changes you have made to your models.
    - `python manage.py migrate`: Applies the migrations to the database.
- `sqlite3`: The default database used by Django for development and testing.
  - Example:
    - `sqlite3 db.sqlite3`: Opens the SQLite database file in the SQLite command-line interface.
    - `.tables`: Lists all tables in the database.
    - `SELECT * FROM table_name;`: Queries all records from a specific table.
    - `.exit`: Exits the SQLite command-line interface.
    - `PRAGMA table_info(table_name);`: Shows the schema of a specific table.
- `__init__.py`: A file that marks a directory as a Python package, we will use as DRY (Don't repeat yourself) method.
- `settings.py`: Contains all the settings/configuration for this Django project.
  - Example:
    - `DEBUG`: A boolean that turns on/off debug mode.
    - `DATABASES`: A dictionary containing the database configuration.
    - `INSTALLED_APPS`: A list of all Django applications that are activated in this project.
- `urls.py`: Defines the URL patterns for this Django project.
  - Example:
    - `path('admin/', admin.site.urls)`: Routes requests to the Django admin interface.
    - `path('courses/', include('courses.urls'))`: Includes the URL patterns from the `courses` app.
- `wsgi.py`: WSGI **(Web Server Gateway Interface)** An entry-point for WSGI-compatible web servers to serve your project. Only used for Deployment Server.
  - Example:
    - `application = get_wsgi_application()`: Exposes the WSGI callable as a module-level variable named `application`.
- `asgi.py`: ASGI **(Asynchronous Server Gateway Interface)** An entry-point for ASGI-compatible web servers to serve your project. Only used for Deployment Server.
  - Example:
    - `application = get_asgi_application()`: Exposes the ASGI callable as a module-level variable named `application`.


# Create home url as home page

Steps:

1. Create a new file called `views.py` in your `codanics` folder.
2. In `views.py`, define a view function for the home page.

```python
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the home page by Codanics!")
```
3. Open `urls.py` file in your project directory.
4. Import the `home` view (function) from your `views.py` file.
5. Add a new URL pattern for the home page.
   1. `path('home/', home, name='home'),`
   2. `path('', home, name='home'),`

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
]
```
6. Run server `python manage.py runserver`
7. Open your web browser and go to `http://127.0.0.1:8000/home` to see the home page.
8. You should see the message "Welcome to the home page by Codanics!" displayed in your browser.


# Python django migrate command after creating an app
Migrate command in django is used to apply database migrations. Migrations are how Django stores changes to your models (adding a field, deleting a model, etc.) and they are stored as files on disk.

```bash
python manage.py makemigrations # Create new migrations based on the changes you have made to your models
python manage.py migrate # Apply the migrations to the database
```


# admin panel

Admin panel in django gives you:
1. A user-friendly interface to manage your application's data.
2. The ability to add, edit, and delete records in your database.
3. Built-in support for authentication and permissions.
4. Customization options to tailor the admin interface to your needs.

You need credentials:

```bash
python manage.py createsuperuser
```

# database and model for courses app

1. Open `models.py` file in your `courses` app directory.
2. Define your models (database tables) using Django's ORM (Object-Relational Mapping) system.
```python
from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course_image = models.ImageField(upload_to='images/')
    difficulty_level = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    instructor = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
```
3. Run the following command to create the necessary database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```
4. Verify that the tables have been created in your database.
```bash
python manage.py showmigrations
```
5. Verify that the `Course` model has been created in your database.
```bash
python manage.py dbshell
```
```sql
SELECT * FROM courses_course;
.exit
```




---
<h1 style="font-family: 'poppins'; font-weight: bold; color: Green;">👨‍💻Author: Dr. Muhammad Aammar Tufail</h1>

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/AammarTufail) 
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/muhammadaammartufail) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/dr-muhammad-aammar-tufail-02471213b/)  

[![YouTube](https://img.shields.io/badge/YouTube-Profile-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@codanics) 
[![Facebook](https://img.shields.io/badge/Facebook-Profile-blue?style=for-the-badge&logo=facebook)](https://www.facebook.com/aammar.tufail) 
[![TikTok](https://img.shields.io/badge/TikTok-Profile-black?style=for-the-badge&logo=tiktok)](https://www.tiktok.com/@draammar)  

[![Twitter/X](https://img.shields.io/badge/Twitter-Profile-blue?style=for-the-badge&logo=twitter)](https://twitter.com/aammar_tufail) 
[![Instagram](https://img.shields.io/badge/Instagram-Profile-blue?style=for-the-badge&logo=instagram)](https://www.instagram.com/aammartufail/) 
[![Email](https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email)](mailto:aammar@codanics.com)
