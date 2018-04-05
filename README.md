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

Athletes
	
	[GET] Used to retrieve info
	All: http://127.0.0.1:8000/api/sporta/athletes/
	One: http://127.0.0.1:8000/api/sporta/athletes/<user_id>

	[POST] Used to create 
	http://127.0.0.1:8000/api/sporta/athletes/
	
	Input: 
	{
		"bio": "enter bio here"
	}


	[PUT] Used to edit current data
	
	Input: Same as above 

Teams

	[GET] Used to retrieve info
	All : http://127.0.0.1:8000/api/sporta/teams/
	One : http://127.0.0.1:8000/api/sporta/teams/<team_id>
	
	[POST] Used to create 
	http://127.0.0.1:8000/api/sporta/teams/
	
	Input:
	{
		"name": "input name here",
		"abbrev" : "input 3 letter abbreviation here",
		"bio" : "enter team bio here",
		"primary_color" : "enter team primary color here",
		"secondary_color" : "enter team secondary color here"
	}

	[PUT] Used to edit current data
	http://127.0.0.1:8000/api/sporta/teams/

	Input: Not all needs to be filled out

	Input:
	{
		"id" : <league_id>,
		"name": "input name here",
		"abbrev" : "input 3 letter abbreviation here",
		"bio" : "enter team bio here",
		"primary_color" : "enter team primary color here",
		"secondary_color" : "enter team secondary color here"
	}

	
	TEAM ADMIN SECTION (all are [POST] requests)
	
	Adding an athlete: http://127.0.0.1:8000/api/sporta/teams/<team_id>/add_athlete/
	
	Input:
	{
		"user_id" : <id of athlete here>
	}



	Removing an athlete : http://127.0.0.1:8000/api/sporta/teams/<team_id>/remove_athlete/

	Input: Same as above
	
		
	Suspending an athlete : http://127.0.0.1:8000/api/sporta/teams/<team_id>/suspend_athlete/

	Input: Same as above

	
	Changing the team name: http://127.0.0.1:8000/api/sporta/teams/<team_id>/change_name/
	
	Input:
	{
		"name" : "new team name here"
	}


	Changing the team colors: http://127.0.0.1:8000/api/sporta/teams/<team_id>/change_colors/

	Input: 
	{
		"primary_color": "color",
		"secondary_color": "color"
	}

Leagues

	[GET] Used to retrieve info
	All : http://127.0.0.1:8000/api/sporta/leagues/leagues/
	One : http://127.0.0.1:8000/api/sporta/leagues/leagues/<league_id>

	[POST] Used to create
	http://127.0.0.1:8000/api/sporta/leagues/leagues/

	Input:
	{
		"name" : "name here"
		"abbrev": "3 letter league abbreviation",
		"bio": "league bio",
		"league_start": "league start date",
		"league_end": "league end date",
		"playoff_start": "playoff start date",
	}

	[PUT] Used to edit 
	http://127.0.0.1:8000/api/sporta/leagues/leagues/

	Input: Not all needs to be filled out
	{
		"id" : <league_id>,
		"name" : "name here",
		"abbrev": "3 letter league abbreviation",
		"bio": "league bio",
		"league_start": "league start date",
		"league_end": "league end date",
		"playoff_start": "playoff start date",
	}
	
	LEAGUE ADMIN SECTION (all are [POST] requests)
	
	Adding an athlete (for team placement?): http://127.0.0.1:8000/api/sporta/leagues/leagues/add_athlete/
	
	Input:
	{
		"user_id" : <id of athlete here>
	}

	
	Removing an athlete (from team placement?): http://127.0.0.1:8000/api/sporta/leagues/leagues/remove_athlete/

	Input: Same as above

	
	Suspending an athlete : http://127.0.0.1:8000/api/sporta/leagues/leagues/suspend_athlete/

	Input:
	{
		"user_id": <athlete id of user being suspended>
		"team_id" : <team id the user belongs to>
	}

	
	Changing League name : http://127.0.0.1:8000/api/sporta/leagues/leagues/change_name/

	Input:
	{
		"name" : "new name here"
	}

	
	Changing League colors : http://127.0.0.1:8000/api/sporta/leagues/leagues/change_color/

	Input: 
	{
		"primary_color": "color",
		"secondary_color": "color"
	}

Divisions in Leagues
	
	[GET] Used to retrieve info
	All : http://127.0.0.1:8000/api/sporta/leagues/divisions/
	One : http://127.0.0.1:8000/api/sporta/leagues/divisions/<division_id>

	[POST] Used to create
	http://127.0.0.1:8000/api/sporta/leagues/divisions/

	Input:
	{
		"name" : "name here"
		"abbrev": "3 letter league abbreviation",
		"league_id": <league_id>
	}

	[PUT] Used to edit 
	http://127.0.0.1:8000/api/sporta/leagues/leagues/<divisions>/

	Input: 
	{
		"id": <division_id>,
		"name" : "name here",
		"abbrev": "3 letter league abbreviation",
		"league_id": <league_id>
	}


	DIVISION ADMIN SECTION (Based on league owner permissions)


	Adding a team

	Removing a team

	Changing division name


	

