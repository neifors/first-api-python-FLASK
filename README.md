### Study Notes
[Python as a Backend: Flask](https://github.com/getfutureproof/fp_guides_wiki/wiki/Flask)

# Exercises
1. Create a Flask API
   - You can choose what it does!
   - Your API should respond to at least one GET and one POST request
   - Add at least one extension eg. a database connection or an email service
   - Follow documentation to add some tests using [pytest](https://pytest-flask.readthedocs.io/en/latest/features.html)

2. Prepare a short (3-5 minute) demonstration of your new API
    - Focus on demonstrating your API's functionality
    - You could demonstrate using curl, Hoppscotch, a custom client or a combination!

# Run Demo

- `cd flask-demo` 
- `pipenv install -r requirements.txt`
- `pipenv shell`
- Tell terminal which application to work with:
   - `export FLASK_APP=server.py` _(Linux/MacOS/GitBash)_ 
   - `set FLASK_APP=server.py` _(Windows Command Prompt)_ 
   - `$env:FLASK_APP = "server.py"` _(PowerShell)_
- Tell terminal which environment to work in:
   - `export FLASK_ENV=development` _(Linux/MacOS/GitBash)_ 
   - `set FLASK_ENV=development` _(Windows Command Prompt)_ 
   - `$env:FLASK_ENV="development"` _(PowerShell)_
- `flask run`
