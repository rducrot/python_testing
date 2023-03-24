from datetime import datetime

from flask import Flask, render_template, request, redirect, flash, url_for

from gudlft.models import load_clubs, load_competitions

app = Flask(__name__)
app.config.from_object('config')

competitions = load_competitions('gudlft/data/competitions.json')
clubs = load_clubs('gudlft/data/clubs.json')

MAX_PLACES_PER_CLUB = 12


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/show-summary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        flash("Unknown or missing mail address.")
        return redirect(url_for('index'))


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if datetime.strptime(found_competition['date'], '%Y-%m-%d %H:%M:%S') < datetime.now():
        flash("Competition is over")
    else:
        if found_club and found_competition:
            return render_template('booking.html', club=found_club, competition=found_competition)
        else:
            flash("Something went wrong-please try again")

    return render_template('welcome.html', club=found_club, competitions=competitions)


@app.route('/purchase-places', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]

    if request.method == 'POST':
        places_required = int(request.form['places'])

        if places_required > int(competition['numberOfPlaces']):
            flash('Not enough remaining places.')
        elif places_required > int(club['points']):
            flash('You do not have enough points.')
        elif places_required > MAX_PLACES_PER_CLUB:
            flash(f'You cannot book more than {MAX_PLACES_PER_CLUB} places.')
        else:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
            club['points'] = int(club['points']) - places_required
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)

        return render_template('booking.html', club=club, competition=competition)


@app.route('/clubs-points')
def clubs_points():
    return render_template('clubs_points.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
