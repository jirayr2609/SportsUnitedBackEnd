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
	
# Active Enpoints
[GET] ENDPOINTS

Athletes:

	Get all
	http://127.0.0.1:8000/api/sporta/athletes/

	Get specific
	http://127.0.0.1:8000/api/sporta/athletes/user_id/

Teams:

	Get all
	http://127.0.0.1:8000/api/sporta/teams/

	Get specific
	http://127.0.0.1:8000/api/sporta/teams/team_id/

Leagues:

	Get all
	http://127.0.0.1:8000/api/sporta/leagues/leagues/

	Get specific
	http://127.0.0.1:8000/api/sporta/leagues/leagues/league_id/

User Info:
	
	Get by id:
	http://127.0.0.1:8000/api/sporta/accounts/user/<user_id>/


[POST] ENDPOINTS

User:

	Verify Username:
	http://127.0.0.1:8000/api/sporta/accounts/verify-username/

	Send:
	{
		"username": "username",
	{

	Returns:
	{
		"available": "true/false",
	}


Athletes:

	Create
	http://127.0.0.1:8000/api/sporta/athletes/
	Send:
	{
            	'user': user,
            	'bio': bio,
        }

Teams:

	Create
	http://127.0.0.1:8000/api/sporta/teams/
	Send:
	{
            	'name': ,
            	'abbrev': ,
            	'bio': ,
            	'created_at': ,
            	'updated_at': ,
        }
Leagues:

	Create
	http://127.0.0.1:8000/api/sporta/leagues/leagues/
	Send:
	{
            	'name': ,
            	'abbrev': ,
            	'bio': ,
            	'league_start': ,
            	'league_end': ,
            	'playoff_start': ,
        }

[PUT] ENDPOINTS

	Update League:
	http://127.0.0.1:8000/api/sporta/leagues/leagues/
	Send:
	{
            	"id": "league_id",
            	"name": "",
            	"abbrev": "",
            	"bio": "",
            	"league_start": "",
            	"league_end": "",
            	"playoff_start": "",
        }

	Update Team:
	http://127.0.0.1:8000/api/sporta/teams/
	{
	
        	'name':,
            	'abbrev': ,
            	'bio': ,
            	'created_at': ,
            	'updated_at': ,
        }

	Update Athlete:
	http://127.0.0.1:8000/api/sporta/athletes/
	{
            	'user': user,
            	'bio': bio,
        }


