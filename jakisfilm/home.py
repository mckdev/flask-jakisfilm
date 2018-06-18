from flask import Blueprint, render_template

from jakisfilm.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/')
def home():

    db = get_db()
    movie_count = db.execute(
        'SELECT COUNT(*)'
        ' FROM movie'
    ).fetchone()

    return render_template(
        'home/home.html',
        movie_count=movie_count[0])
