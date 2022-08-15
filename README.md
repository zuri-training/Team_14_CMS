# Content Management System (CMS_Team_14)

<p align="center">
  <img width="1000" height="300" src="https://github.com/zuri-training/Team_14_CMS/blob/main/template/signinPage/signin-logo.svg">
</p>

## Steps

## Aim
This project is expected to allow users to create or spin up a basic website.

## Google Docs Link Including Meetings Information etc. 
[Documentation](https://docs.google.com/document/u/0/d/11qXZp9zK4tGaMCZRzA6e-6c6V6iFT2bUUeJFTzksjG0/mobilebasic)

## db schema:
[Database Schema](https://cacoo.com/diagrams/3bidFKDK0MhYkbBU/B208B?reload_rt=1659123507956_0&reload_dc=1659139986069_0)

## figma design:

[design](https://www.google.com/url?q=https://www.google.com/url?q%3Dhttps://www.figma.com/file/KUXA9TjkYyUWDkSNTewHbU/CMS%26amp;sa%3DD%26amp;source%3Deditors%26amp;ust%3D1659469559838528%26amp;usg%3DAOvVaw1VT_BeRd1sxOaw2FH4Zhsw&sa=D&source=docs&ust=1659469559887420&usg=AOvVaw2JIALqcELgklhbtcRQelAr)

## How To Run
 To run locally on your machine, you can use the following command:

Clone the repository

	git clone https://github.com/zuri-training/Team_14_CMS.git
	
Move to the project folder

	cd Team_14_CMS

Create a Virtual environment

	Virtualenv env

Activate the Virtual environment

	env/Scripts/activate or env/bin/activate

Install Dependencies

	pip install -r requirements.txt

Migrate Datebase

	python manage.py migrate

Create Superuser

	python manage.py createsuperuser

Finally, run  server

	python manage.py runserver

## Feature Requested By Zuri

# deploy to a server with nginx using gunicorn
	sudo -u postgres psql
	CREATE DATABASE myproject;
	CREATE USER myprojectuser WITH PASSWORD 'password';
	ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
	ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
	ALTER ROLE myprojectuser SET timezone TO 'UTC';
	GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
	quit postgreSql with \q;
### install the required packages to deploy with:
	pip install gunicorn psycopg2-binary
### edit the prjectdir and include required files
	sudo nano ~/myprojectdir/myproject/settings.py
	ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . ., 'localhost']
	DATABASES = {
       'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
     }
  }
  STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
 
### migrate again
	~/myprojectdir/manage.py makemigrations
	~/myprojectdir/manage.py migrate
### collectstatic files
	python manage.py collectstatic
## allow port if not done
	sudo ufw allow 8000
### test localhost
	python manage.py runserver 0.0.0.0:8000
	
### finally bind gunicorn
	gunicorn --bind 0.0.0.0:8000 csmproject.wsgi

1. User: Unauthenticated
	- Visit the platform to view basic information about it
	- View and Interact with the documentation
	- Register to setup a new website
	- Setup website by filling out some information
	- Browse through available templates 
2. User: Authenticated
	- Full access to the platform
	- Access to backend of created website
	- Ability to create more pages
	- Ability to change template
	- Unique address
	- Ability to add social media links
