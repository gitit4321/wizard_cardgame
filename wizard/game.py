from wizard.wizard_game.round import Round
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


round = Round(20, 3, 0)
round.deal_hands()
deck = round.deck
trump = round.set_trump()


@bp.route('/play', methods=('GET', 'POST'))
@login_required
def play():

    if request.method == 'POST':
        if 'bid-0' in request.form:
            player = 0
            bid = request.form['bid-0']
        elif 'bid-1' in request.form:
            player = 1
            bid = request.form['bid-1']
        elif 'bid-2' in request.form:
            player = 2
            bid = request.form['bid-2']
        elif 'bid-3' in request.form:
            player = 3
            bid = request.form['bid-3']
        elif 'bid-4' in request.form:
            player = 4
            bid = request.form['bid-4']
        elif 'bid-5' in request.form:
            player = 5
            bid = request.form['bid-5']

        error = None

        if not bid:
            error = 'A bid is required.'

        if error is not None:
            flash(error)
        else:
            # print(request.form.keys())
            print(f"Bid was {bid}")
            round.set_bid(player, int(bid))
            return redirect(url_for('game.play'))

    return render_template('game/play.html', round=round, hands=round.player_hands, deck=deck, trump=trump, handsize=round.hand_size)
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
