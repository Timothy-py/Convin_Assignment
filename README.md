# Convin_Assignment
This is a backend project assignment for Convin internship application

In this assignment, you will be implementing the following two systems using
Django
1. Create a model having fields of type CharField and FileField.
Implement a system on top of this model which should notify the
updated/created field only and its old and new value. (it shouldn’t notify about
the field which is not updated). It should also notify in case content of FileField
is changed. [You may use signals or any other mechanism of your choice.]
2. Now suppose CharField is the encrypted value of the content of
FileFIeld (or you can choose any heavy computation of your choice on the
content of File(it may be just along for loop)). Implement a system which allows
updating FileField content by an external party (for example invoking
management command from bash or calling a Django API or your choice of
making it accessible by an external party). Note: after FileField content is
changed, it should notify the updated value of FileField and CharField.

## Clone the repository
git clone https://github.com/Timothy-py/Convin_Assignment.git

## Create a virtual environment and activate git
virtualenv <environment_name>

## Install the requirements
python install -r requirements.txt

## Run migrations
python manage.py makemigrations system1
python manage.py migrate

## Create a superuser to access the admin page
python manage.py createsuperuser

## Run the server
python manage.py runserver

### API endpoint for file field update
localhost:80000/api/update/<pk>

### 1. Django admin UI to add a new file
<img src="media/Screenshot(24).png">

### 2. New file created showing the encrypted file field
<img src="media/Screenshot(26).png">

### 3. Updating the file field with the API
<img src="media/Screenshot(28).png">



