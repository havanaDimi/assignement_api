# Assignement api for vcf data manipulation

This is a simple API to allow users to navigate through the data of a vcf file, view. Only authorized users can create, edit and delete records in the system.

# Quickstart
python3 -m venv env

`source env/bin/activate`  # On Windows use `env\Scripts\activate`

`pip install -r requirements.txt`

`python manage.py runserver`

# UI navigation
The service is up and running locally on 127.0.0.1/vcfs/

You can view the records as json or xml.


In case you want to post a new record, you can login via the respective button and use the credentials 

username: admin 

password:test123

If you want to select details for a vcf with a specific ID you can navigate through url (ex. 127.0.0.1/vcfs/rs123/)

If you have authentication priviledges you can update or delete the record(s).


