# Assignment api for vcf data manipulation
This is a simple API to allow users to navigate through the data of a vcf file, view. Only authorized users can create, edit and delete records in the system.

# Quickstart

Download this project on your local machine.

`cd /replace_with_your_directory/assignement_api-master/`

`python3 -m venv env`

`source env/bin/activate`  # On Windows use `env\Scripts\activate`

`pip install -r requirements.txt`

`python manage.py runserver` (# This command should run in the directory  that is the manage.py file)

# UI web browser navigation
The service is up and running locally on `127.0.0.1:8000`. You have the option to view it in your web browser.

Recommended Steps:
1. Please add your vcf file in the application direcotry in order to upload it in the database. (your_directory\assignement_api-master\vcf_handler\files). (It is recommended to have one vcf file at a time in the folder)

2. Visit `127.0.0.1/read_file/` in order to handle the vcf file and navigate you to the list of records in the vcf (`127.0.0.1/vcfs/`). (If no vcf file found on the directory, an empty list of records is appeared.)

You can view the records as json or xml, via the respective option buttons.

3. If you want to select details for a vcf with a specific ID you can navigate through url (ex. `127.0.0.1/vcfs/rs123/`). If no record found with the specific ID, a response error is appeared.

4. In case you want to post a new record, you can login via the respective button (up and right in the template) and use the credentials 

username: admin 

password:test123

5. For a specific record ID, if you have authentication priviledges (after sucessfully login) you can update or delete the record(s), via the respective PUT and DELETE buttons.

* You have the option to run tests for the application via `python manage.py test`

* All the above navigation can be test with curl or httpie requests using the rellated headers, authorization credetials etc.
