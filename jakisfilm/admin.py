from flask import (Blueprint, flash, g, redirect, render_template, request,
                   url_for)
from werkzeug.exceptions import abort
from jakisfilm.db import get_db


bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    page_title = 'Movies'
    
    db = get_db()
    movies = db.execute(
        'SELECT m.id, created, title, youtube_id'
        ' FROM movie m'
        ' ORDER BY created DESC'
    ).fetchall()

    return render_template(
        'admin/index.html',
        movies=movies,
        page_title=page_title)

@bp.route('/add', methods=('GET', 'POST'))
def add():
    page_title = 'Add Movie'

    if request.method == 'POST':
        title = request.form['title']
        youtube_id = request.form['youtube_id']
        error = None
    
        if not title:
            error = 'Title is required.'
        
        if not youtube_id:
            error = 'Youtube ID is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO movie (title, youtube_id)'
                ' VALUES (?, ?)',
                (title, youtube_id)
            )
            db.commit()
            return redirect(url_for('admin.index'))

    return render_template('admin/add.html', page_title=page_title)


def get_movie(id):
    movie = get_db().execute(
        'SELECT m.id, created, title, youtube_id'
        ' FROM movie m'
        ' WHERE m.id = ?', (id,)
    ).fetchone()

    if movie is None:
        abort(404, "Movie id {0} doesn't exist.".format(id))

    return movie


@bp.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    page_title = 'Edit Movie'

    movie = get_movie(id)

    if request.method == 'POST':
        title = request.form['title']
        youtube_id = request.form['youtube_id']
        error = None

        if not title:
            error = 'Title is required.'

        if not youtube_id:
            error = 'Youtube ID is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE movie SET title = ?, youtube_id = ?'
                ' WHERE id = ?',
                (title, youtube_id, id)
            )
            db.commit()
            return redirect(url_for('admin.index'))

    return render_template('admin/edit.html', movie=movie)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_movie(id)
    db = get_db()
    db.execute('DELETE FROM movie WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('admin.index'))
