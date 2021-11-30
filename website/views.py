from flask import render_template, Blueprint, redirect, url_for, request
import time
from descriptions import descriptions, patient, wonder

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template('home.html')


@views.route('/calendar')
def calendar():
    day = int(time.strftime('%d'))
    month = int(time.strftime('%m'))
    day = 1  # REMOVE/COMMENT THIS LINE IN PRODUCTION
    if day in [1, 21]:
        ending = 'st'
    elif day in [2, 22]:
        ending = 'nd'
    elif day in [3, 23]:
        ending = 'rd'
    else:
        ending = 'th'
    return render_template('calendar.html', descriptions=descriptions, patient=patient, wonder=wonder, day=day, ending=ending, month=month)


@views.route('/today')
def today():
    day = int(time.strftime('%d'))
    month = int(time.strftime('%m'))
    hour = int(time.strftime('%H'))
    year = int(time.strftime('%Y'))

    if month != 12 and year == 2021:
        return render_template('early.html')
    elif year > 2021 or (day > 24 and month == 12):
        return redirect(url_for('views.calendar'))
    elif year == 2021 and month == 12 and hour >= 6:
        return redirect(f'day/{day}')


@views.route('day/<request_day>')
def day(request_day: str):
    request_day = int(request_day)
    day = int(time.strftime('%d'))
    month = int(time.strftime('%m'))
    hour = int(time.strftime('%H'))
    year = int(time.strftime('%Y'))

    try:
        user_name = request.headers['X-Replit-User-Name']
        user_id = request.headers['X-Replit-User-Id']
    except KeyError:
        user_name = False
        user_id = False

    # REMOVE/COMMENT THIS LINE IN PRODUCTION
    return render_template(f'days/{request_day}.html', day=request_day, user_name=user_name, user_id=user_id)

    if month != 12 and year == 2021:
        return render_template('early.html')
    elif year > 2021 or (day > 24 and month == 12) or (request_day > day and month == 12) or (request_day == day and month == 12 and hour >= 6):
        return render_template(f'days/{request_day}.html', day=request_day, user_name=user_name, user_id=user_id)


@views.route('/credits')
def credits():
    return render_template('credits.html')
