# A Google classroom assignments manager using Google Classroom API

### What you can do through the application
+ View all your pending work (including missed deadlines)
+ View assigned grades for work you submitted
+ View Notifications for each active Unit
+ View your grades progress on chart (average per unit)
+ Submit assignments (with proper permissions)
+ Unsubmit assignments (with proper permissions)

See video demo: https://youtu.be/LD90tDF5B9Y?si=I8_azjUMfIkIMRvt

## Implementation
I utilized the Google classroom API to get resources such as courses, coursework, student submissions, notifications and captured required information from these resources then sent to the React frontend using Django function-based api views

I also used Google Drive API to upload files to Google drive then submitting the files to google classroom since the submission object for files require a file id to be a google drive id

Authentication was handled by Google Oauth through the Oauth consent screen


## NB: SUBMITTING ASSIGNMENTS
- The Classroom API requires you to be the owner of a coursework to be able to modify assignment attachments, meaning you have to be the creator of the assignment to be able to modify the work. This means that students can only view information about their submissions but they can't submit work through the API, i realized this mid project :(. Hopefully there'll be a classroom API functionality for student submissions soon.
- For more info, see the docs: https://developers.google.com/classroom/reference/rest/v1/courses.courseWork.studentSubmissions

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
    |__ run.sh


    assigno_manager/
    ├── asgi.py
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


## How to run
### Linux
- To be added to **test users**, send an email to alphaian020@gmail.com. Since this is a google cloud console project in test mode, only allowed users can access the API functionalities.

Because of many unassigned grades, your progress report chart reports could be minimal (or none)
- To view test data and see how it looks like on the chart, start the app with
```python
./run.sh
```

- To view your real data (your real unit average grades) on the chart, start the app with
```python
USE_CHART_DATA=REAL ./run.sh
```

### MacOs / Windows
In progress
