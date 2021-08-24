### Study Notes
| [Python as a Backend: Flask](https://github.com/getfutureproof/fp_guides_wiki/wiki/Flask) | [Testing with Pytest](https://github.com/getfutureproof/fp_guides_wiki/wiki/Testing-with-Pytest) |

# Exercises
1. Create a Flask API
   - You can choose what it does!
   - Your API should respond to at least one GET and one POST request
   - Follow documentation to add some tests using [pytest](https://pytest-flask.readthedocs.io/en/latest/features.html)
   - Research and start implementation of at least one extension or additional feature eg. a database connection, an email service, deployment

2. Prepare a short (3-5 minute) demonstration of your new API
    - Focus on demonstrating your API's functionality
    - You could demonstrate using curl, Hoppscotch, a custom client or a combination!

# Run Demo

_NB: These instructions assume you have Pipenv installed within your current version of Python. For non-Pipenv users, a `requirements.txt` is provided, including dev dependencies._
- `pipenv shell`
- `pipenv install --dev`
- Run dev server with `pipenv run dev`
- Run prod server with `pipenv run start`
- Run tests with `pipenv run test`
- Get coverage report with `pipenv run coverage`

Available routes: \
`GET`, `POST`: `/api/cats` \
`GET`, `PATCH`, `PUT` ,`DELETE`: `/api/cats/:id`

--

**If you are having issues with the dev script, start your server with the following**
- Tell terminal which environment to work in:
   - `export FLASK_ENV=development` _(Linux/MacOS/GitBash)_ 
   - `set FLASK_ENV=development` _(Windows Command Prompt)_ 
   - `$env:FLASK_ENV="development"` _(PowerShell)_
- `flask run`
