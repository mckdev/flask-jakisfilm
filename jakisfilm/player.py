from flask import Blueprint, render_template
from jakisfilm.db import get_db


bp = Blueprint('player', __name__, url_prefix='/player')


@bp.route('/')
def index():
    page_title = 'Player'
    
    db = get_db()
    movie = db.execute(
        'SELECT m.title, youtube_id'
        ' FROM movie m'
        ' ORDER BY RANDOM()'
        ' LIMIT 1'
    ).fetchone()

    return render_template(
        'player/player.html',
        movie=movie,
        page_title=page_title)
