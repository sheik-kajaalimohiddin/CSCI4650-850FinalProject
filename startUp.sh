#!/bin/bash
###Install necessary dependencies###
sudo yum install python -y &> /dev/null
sudo yum install git -y &> /dev/null
sudo yum install pip -y &> /dev/null
sudo pip install virtualenv &> /dev/null
pip install --upgrade pip &> /dev/nulll
DIR1="eb-virt"
if [ -d "DIR1" ];
then
	source ~/eb-virt/bin/activate
	pip install Django &> /dev/null
	pip install django-crispy-forms &> /dev/null
	python -m pip install Pillow &> /dev/null
	pip install bootstrap &> /dev/null
	pip install psycopg2-binary &> /dev/nul
else
	virtualenv ~/eb-virt &> /dev/null
	source ~/eb-virt/bin/activate
	pip install Django &> /dev/null
	pip install django-crispy-forms &> /dev/null
	python -m pip install Pillow &> /dev/null
	pip install bootstrap &> /dev/null
	pip install psycopg2-binary &> /dev/nul
fi

DIR="CSCI4650850FinalProject"

if [ -d "$DIR" ];
then
	rm -rf CSCI4650850FinalProject/
	git clone https://github.com/sheik-kajaalimohiddin/CSCI4650850FinalProject.git &> /dev/null
	cd CSCI4650850FinalProject/
	python manage.py makemigrations &> /dev/null
	python manage.py migrate &> /dev/null
	python manage.py runserver 0.0.0.0:8000 &> /dev/null
else
	git clone https://github.com/sheik-kajaalimohiddin/CSCI4650850FinalProject.git &> /dev/null
	cd CSCI4650850FinalProject/
	python manage.py makemigrations &> /dev/null
	python manage.py migrate &> /dev/null
	python manage.py runserver 0.0.0.0:8000 &> /dev/null
fi