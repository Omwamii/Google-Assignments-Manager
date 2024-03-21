# A Google classroom assignments manager using Google Classroom API

### What you can do through the application
+ View all your pending work (including missed deadlines)
+ View assigned grades for work you submitted
+ View Notifications for each active Unit
+ View your grades progress on chart (average per unit)
+ Submit assignments (with proper permissions)
+ Unsubmit assignments (with proper permissions)

## How I did it
I utilized the Google classroom API to get resources such as courses, coursework, student submissions, notifications and captured required information from these resources then sent to the React frontend using Django function-based api views

I also used Google Drive API to upload files to Google drive then submitting the files to google classroom since the submission object for files require a file id to be a google drive id

Authentication was handled by Google Oauth through the Oauth consent screen

## File structure
### Important files organization

    ./
    |__ assigno_manager/
    |__ credentials.json
    |__ db.sqlite3
    |__ g-assigns/
    |__ manage.py
    |__ mysubs/
    |__ requirements.txt
    |__ README.md


    assigno_manager/
    ├── asgi.py
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   ├── settings.cpython-311.pyc
    │   ├── urls.cpython-311.pyc
    │   └── wsgi.cpython-311.pyc
    ├── settings.py
    ├── urls.py
    └── wsgi.py


    mysubs
    ├── admin.py
    ├── app.py
    ├── apps.py
    ├── base.py
    ├── course.py
    ├── data
    │   └── stats.json
    ├── files.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── regex.py
    ├── tests.py
    ├── urls.py
    └── views.py

    g-assigns/src
    ├── App.js
    ├── App.test.js
    ├── Grades.js
    ├── Home.js
    ├── index.css
    ├── index.js
    ├── Navbar.js
    ├── NoPage.js
    ├── Notifs.js
    ├── PendingCache.js
    ├── reportWebVitals.js
    ├── setupTests.js
    ├── Stats.js
    └── UnitsCache.js


*models.py* - contains one model 'MarkAsDone' which keeps track of assignments which are marked as Done

*views.py* - contains the api views that handle api requests to the backend

*urls.py* - contains url configurations

*base.py* - contains the Base Class for app resources initializations and authentication

*course.py* - contains the Course class, inheriting from base that handles course information resources

*file.py* - contains the Files class, which handles file operations like submission, unsubmission

*app.py* - contains the final App class, inheriting from Files

*admin.py* - contains registered models on the admin site

*regex.py* - contains a function which uses regex to extraxt course code name from a complete course description

*g-assigns/src/* * - contains React component files

## How to run
- After cloning, make sure all packages necessary are installed by typing
```python
pip install -r requirements.txt
```
- To be added to **test users**, send an email to alphaian020@gmail.com. Since this is a google cloud console project, only allowed users can access the API functionalities.

Because of many unassigned grades, your progress report chart reports could be minimal (or none)
- To view test data and see how it looks like on the chart, start the backend server with:
```python
gunicorn assigno_manager.wsgi:application --timeout 60
```

- To view your real data (your real unit average grades) on the chart, start the backend server with
```python
USE_CHART_DATA=REAL gunicorn assigno_manager.wsgi:application --timeout 60
```

- In another tab, from the root folder, move to frontend folder and install the packages with
```
cd g-assigns ; npm install
```
- Start the frontend server
```python
npm start
```
