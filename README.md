Property Sales Management
The primary objective of this project would be to build a property sales website for both seller and buyer.
create a .env file credentials with details
export MYSQL_HOST='<MYSQL_HOST>'
export MYSQL_USER='<MYSQL_USER>'
export MYSQL_PASS='<MYSQL_PASS>'
export MYSQL_DB='<MYSQL_DB>'
export MYSQL_PORT=<MYSQL_PORT>
Run Locally
Pull from 'project-setup' branch
  git pull origin project-setup
create a virtual environment

  python -m venv venv
activate the virtual environment

  .\venv\Scripts\activate
Install dependencies

  pip install -r requirements.txt
Setup Django
go to property_sales folder

  cd property_sales
Given database name in .env file will be going to create a database automatically if not exists.

  python create_db.py
Migrate the Database for creating tables by django commands

  python manage.py makemigrations
  python manage.py migrate
Run the server
  python manage.py runserver
Tech Stack
Client: HTML, CSS, Bootstrap,Javascript

Framework: Django

Database: MySQL Database
