#!/bin/env bash

# Scripts to get everything ready & start the server

# Function to stop Django's 'manage.py runserver' process and backend/frontend servers
stop_servers_linux() {
    echo -e "\n\e[32mStopping Django server...\e[0m"
    
    # Find and kill the 'manage.py runserver' processes
    pids=$(ps aux | grep 'manage.py runserver' | grep -v grep | awk '{print $2}')
    
    if [ -n "$pids" ]; then
        for pid in $pids; do
            kill "$pid"
        done
        echo -e "\e[33mDjango server stopped.\e[0m"
    fi
    
    echo -e "\n\e[32mStopping backend server port (8000)...\e[0m"
    kill $(lsof -t -i:8000) 2>/dev/null
    echo -e "\e[33mBackend server stopped.\e[0m"
    
    echo -e "\n\e[32mStopping frontend server port (3000)...\e[0m"
    kill $(lsof -t -i:3000) 2>/dev/null
    echo -e "\e[33mFrontend server stopped.\e[0m"
}

# Function to stop app servers running on specific ports (Windows)
stop_servers_windows() {
    echo -e "\n\e[31mStopping backend server...\e[0m"
    # Windows-specific server stop logic here
}

# Trap interrupt signal (Ctrl+C)
trap_interrupt() {
    echo -e "\n\e[32mScript interrupted. Stopping servers...\e[0m"

    # Determine OS and call appropriate stop_servers function
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        stop_servers_linux
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
        stop_servers_windows
    else
        echo -e "\e[31mUnsupported operating system: $OSTYPE\e[0m"
    fi

    exit 1
}

# Trap interrupt signal (Ctrl+C)
trap trap_interrupt INT


echo -e "\n\e[36mInstalling Python dependencies...\e[0m\n"
pip3 install -r requirements.txt

# echo  -e "\e[36mStarting Gunicorn server...\e[0m\n"

if [ "$USE_CHART_DATA" = "REAL" ]; then
	echo -e "\n\e[36mUsing real student data to fetch stats...\e[0m\n"
	# USE_CHART_DATA=REAL gunicorn assigno_manager.wsgi:application --timeout 60 &         -- windows machines no gunicorn
	USE_CHART_DATA=REAL python3 manage.py runserver &
	wait
else
	echo -e "\n\e[36mUsing dummy data to fetch stats...\e[0m\n"
	# gunicorn assigno_manager.wsgi:application --timeout 60 &
	python3 manage.py runserver &
	wait
fi

echo -e "\e[36mInstalling Node.js dependencies...\e[0m\n"
cd g-assigns

if [ -d node_modules ]; then
	# avoid running npm install when unnecessary
	echo -e "\e[31mNode modules already installed...\e[0m\n"
else
	npm install
fi

echo -e "\e[32mstarting frontend server...\e[0m"
npm start
