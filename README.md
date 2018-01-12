# SportsUnitedBackEnd
SportsUnited back end source code 

## INSTRUCTIONS
### These commands work for linux and mac

If you dont have python 3 installed in your computer | brew requires installation if you dont have it.
	
	brew install python3

Otherwise

	git clone ...
	cd SportsUnitedBackEnd

Must install virtual environment to run app
Make sure that you run the following commads where src/ is located

	virtualenv -p python3 env
	source env/bin/activate

	pip install django==2

	cd src

	python manage.py runserver 0:8000