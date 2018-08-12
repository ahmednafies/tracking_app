#!/bin/bash


function firstTime {
	echo "First time"
	
	echo "activate virtual environment"
	source ../venv/bin/activate
	
	cd kuhne_shipit
	echo "Model migrations"
	python manage.py makemigrations
	python manage.py migrate
	
	echo "create suoer user"
	python manage.py createsuperuser
		
	echo "load database"
	python manage.py loaddata shipments/fixtures/initial.json
	
	echo "run tests"
	python manage.py test

	echo "run server"
	python manage.py runserver
}


function normalRun {
	echo "normal run"
	echo "äctivate virtual environment"
	source ../venv/bin/activate

	cd kuhne_shipit
	echo "runserver"
	python manage.py runserver
}

while true; do
	read -p "Is it your first time to run the app?" yn
	case $yn in
		[Yy]* ) firstTime ; break;;
		[Nn]* ) normalRun ; break;;
		* ) echo "Please answer yes or no.";;
	esac
done
