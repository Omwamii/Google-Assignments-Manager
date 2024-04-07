#!/bin/env bash

# Scripts to get everything ready & start the server

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Starting Gunicorn server..."
if [ "$USE_CHART_DATA" = "REAL" ]; then
	echo -e "\nUsing real student data to fetch stats...\n"
	# USE_CHART_DATA=REAL gunicorn assigno_manager.wsgi:application --timeout 60 &         -- windows machines no gunicorn
	USE_CHART_DATA=REAL python3 manage.py runserver &
else
	echo -e "\nUsing dummy data to fetch stats...\n"
	# gunicorn assigno_manager.wsgi:application --timeout 60 &
	python3 manage.py runserver &
fi

echo "Installing Node.js dependencies..."
cd g-assigns

if [ -d node_modules ]; then
	# avoid running npm install when unnecessary
	echo "node modules already installed..."
else
	npm install
fi

echo "starting server..."
npm start
