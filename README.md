Django web application that allows users to view, share and manage study resources. 

## Current features

* Users can share files (provided they are logged in) and download files uploaded by other users.
* Users can search in the uploaded content.
* The allowed files types include files with extension .pdf, .doc, .docx, .ppt, .pptx and .txt.
* A user is required to submit title and description of the file to be uploaded.
* The file to be uploaded should be <= 15 MB (all this is configurable within the code).
* Users can manage i.e edit and delete their uploads.
* User can edit their profile.
* Admin pages to regulate the content and manage users and their roles.
* The web-pages are responsive, clean and clutter-free.

## Running the project locally

### Pre-requisites:

* Make sure you have [Python 3](https://www.python.org/downloads/) and pip installed on your system.

### Steps:

1. First, clone the repository to your local machine: 
  
   ```bash
   git clone https://github.com/SudoerRakshit/Django_Notes_Share_App.git
   ```
  
2. Then cd into the folder `django_web_app`(base directory):

   ```bash
   cd django_web_app
   ```

3. Install virtual environment and activate it:
* For Windows:
   ```bash
   pip install virtualenv
   virtualenv venv
   venv\Scripts\activate
   ```
* For Ubuntu Linux:
   ```bash
   sudo apt install virtualenv
   virtualenv -p python3 venv
   source venv/bin/activate
   ```
  
4. Install the dependencies as in `requirements.txt`:
  
   ```bash
   pip install -r requirements.txt
   ```
  
5. Run the development server:</li>

   ```bash
   python manage.py runserver
   ```

6. Now, copy the url http://127.0.0.1:8000 and paste it in your web browser's address bar. 

### Superuser:

7. To log into admin at http://127.0.0.1:8000/admin create a super user:

   ```bash
   python manage.py createsuperuser
   ```
