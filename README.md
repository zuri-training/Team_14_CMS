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

	cd CMS_proj_14

Create a Virtual environment

	Virtualenv env

Activate the Virtual environment

	env/Scripts/activate

Install Dependencies

	pip install -r requirements.txt

Migrate Datebase

	python manage.py migrate

Create Superuser

	python manage.py createsuperuser

Finally, run  server

	python manage.py runserver

## Feature Requested By Zuri

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
	- Ability to add social media link
