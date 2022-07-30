# Content Management System (CMS_Team_14)

## Aim
This project is expected to allow users to create or spin up a basic website

## google docs link including meetings information etc. 
https://docs.google.com/document/u/0/d/11qXZp9zK4tGaMCZRzA6e-6c6V6iFT2bUUeJFTzksjG0/mobilebasic

## db schema:

https://cacoo.com/diagrams/3bidFKDK0MhYkbBU/B208B?reload_rt=1659123507956_0&reload_dc=1659139986069_0


## How To Run
 To run locally on your machine, you can use the following command:

*Clone the repository

git clone https://github.com/zuri-training/Team_14_CMS.git

*Move to the project folder

cd CMS_proj_14

*Create a Virtual environment

Virtualenv env

*Activate the Virtual environment

env/Scripts/activate

*Install Dependencies

pip install -r requirements.txt

*Migrate Datebase

python manage.py migrate

*Create Superuser

python manage.py createsuperuser

*Finally, run  server

python manage.py runserver
