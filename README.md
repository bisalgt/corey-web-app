# corey-web-app
Making a blog website.
Creating superuser only after making database table, by migration
python manage.py makemigrations -- detects the changes and makes django ready for update the database
to apply changes use-- python manage.py migrate
creating database in models
each class of models.py is going to be tables in database
each attributes is going to be field of that database
To view the sql code-- python manage.py sqlmigrate appname migration_number

to work with the database in shell
python manage.py shell