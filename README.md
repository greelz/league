Quick start to see how it all works. 
1. Start the virtual environment (in VS Code, select the interpreter from the venv folder)
2. `pip install -r requirements.txt`
3. Run w/ debugging (F5) OR from within the django folder `python manage.py runserver`
4. When debugging, it will be port `6969`, otherwise default is `8000`

Views that work: 
1. <http://localhost:6969/riot_api/get_matches/greelz/2/>
2. <http://localhost:6969/riot_api/get_puuid/greelz>
