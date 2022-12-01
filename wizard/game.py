from wizard.wizard_game.deck import Deck
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from wizard.auth import login_required
from wizard.db import get_db

bp = Blueprint('game', __name__)


@bp.route('/')
def index():
    db = get_db()
    games = db.execute(
        'SELECT id, title, created'
        ' FROM game'
        ' ORDER BY created DESC'
    ).fetchall()
    # print(games)
    return render_template('game/index.html', games=games)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        # body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO game (title)'
                ' VALUES (?)',
                (title,)
            )
            db.commit()
            return redirect(url_for('game.index'))

    return render_template('game/create.html')


def get_game(id, check_author=True):
    game = get_db().execute(
        'SELECT id, title, created'
        ' FROM game'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if game is None:
        abort(404, f"Game id {id} doesn't exist.")

    # if check_author and post['author_id'] != g.user['id']:
    #     abort(403)

    return game


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    game = get_game(id)

    if request.method == 'POST':
        title = request.form['title']
        # body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE game SET title = ?'
                ' WHERE id = ?',
                (title, id)
            )
            db.commit()
            return redirect(url_for('game.index'))

    return render_template('game/update.html', game=game)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_game(id)
    db = get_db()
    db.execute('DELETE FROM game WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('game.index'))


@bp.route('/play', methods=('GET', 'POST'))
@login_required
def play():
    deck = Deck()
    # print(deck)
    # get_game(id)
    # db = get_db()
    # db.execute('DELETE FROM game WHERE id = ?', (id,))
    # db.commit()
    return render_template('game/play.html', deck=deck)
    # return render_template('game/play.html')

# @bp.route('/<int:id>/play', methods=('GET', 'POST'))
# @login_required
# def play(id):
#     deck = Deck()
#     print(deck)
#     # get_game(id)
#     # db = get_db()
#     # db.execute('DELETE FROM game WHERE id = ?', (id,))
#     # db.commit()
#     # return render_template('game/play.html', deck=deck)
#     return render_template('game/play.html')
