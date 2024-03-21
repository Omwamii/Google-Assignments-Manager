# A Google classroom assignments manager using Google Classroom API

### What you can do through the application
+ View all your pending work (including missed deadlines)
+ View assigned grades for work you submitted
+ View Notifications for each active Unit
+ View your grades progress on chart (average per unit)
+ Submit assignments (with proper permissions)
+ Unsubmit assignments (with proper permissions)

## What I did and why?
Seeing how the google classroom platform is filled with a lot of features, sometimes all a student needs is to see all the pending work, do the work and go ahead and submit it. With the usual classroom, you'd have to first search for the unit, or for those who know, view the assignments tab, but it all seems like a lot of work just to see pending work, let alone missing work

After work is assigned grades, students may not even notice the grades assignment and to which work it was assigned unless they are keen. Through this web application, a student can see grades per unit in an ordely and easy manner without all the overload of assignment instructions and files you submitted, just see what grade you got in which assignment.

Students may also want to see how they are fairing per unit, comparing averages to other units, in one simple click. This is not a feature inculded in google classroom. In my application, users can see their grade averages in a chart with one simple click.

Students also get to see all notifications for units they enrolled in allowing them to quickly make reference for an announcement made with accurate timing

Students, with the proper permissions, are able to submit (turn in) their work using the Google classroom API and also reclaim their work for addition of files.

I decided to create a simple interface for students to quickly see and do what they need efficiently

## How I did it
I utilized the Google classroom API to get resources such as courses, coursework, student submissions, notifications and captured required information from these resources then sent to the React frontend using Django function-based api views

I also used Google Drive API to upload files to Google drive then submitting the files to google classroom since the submission object for files require a file id to be a google drive id

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
    |__ token.json
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


    g-assigns/public
    ├── favicon.ico
    ├── index.html
    ├── logo192.png
    ├── logo512.png
    ├── manifest.json
    └── robots.txt

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

- Start backend server from root of project with: 
```python
gunicorn assigno_manager.wsgi:application --timeout 60
```
- In another tab, from the root folder, move to frontend folder and install the packages with
```
cd g-assigns ; npm install
```
- Start the frontend server
```python
npm start
```
