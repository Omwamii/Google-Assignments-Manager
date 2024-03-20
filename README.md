# A Google classroom assignments manager using Google Classroom API

## What it can do
+ View all your pending work (including missed deadlines)
+ View assigned grades for work you submitted
+ View Notifications for each active Unit
+ View your grades progress on chart (average per unit)
+ Submit assignments (with proper permissions)
+ Unsubmit assignments (with proper permissions)

## How to run
- After cloning, make sure gunicorn is installed. If not, install with
```python
pip install gunicorn
```
- Start backend server from root of project with: 
```python
gunicorn assigno_manager.wsgi:application --timeout 60
```
- In another tab, move to frontend folder and start frontend server
```python
cd g-assigns ; npm start
```
