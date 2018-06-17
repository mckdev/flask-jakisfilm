# JakisFilm

Flask website which plays a random movie from a database of Youtube URLs.

## Development

### Environment

Create virtual environment for the project with Python 3.

Example using virtualenvwrapper:

```
mkvirtualenv -p python3 jakisfilm
workon jakisfilm
```

Install project requirements inside your virtual environment:

```
pip install -r requirements.txt
```

### Create instance config

Create `instance` folder in project root and `config.py` file in it for your instance config.

For example:

```
SITE_NAME="Jakiś Film"
SECRET_KEY="MyVerySecretKey"
```

Note: Public environment variables are stored in `.flaskenv` file.


### Run the app

Run the application with:

```
flask run
```

Access the application by visiting `http://localhost:5000` in your browser.
