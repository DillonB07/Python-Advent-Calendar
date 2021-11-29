from flask import render_template, Blueprint, redirect, url_for
from datetime import datetime
import time
from descriptions import descriptions, patient, wonder
import random

views = Blueprint('views', __name__)

music_files = ['Away In A Manger - Audionautix.mp3', 'Carol Of The Bells - Audionautix.mp3', 'Canon and Variation - Twin Musicom.mp3',
               'Deck the Halls - Kevin MacLeod.mp3', 'Deck the Halls B - Kevin MacLeod.mp3', 'Hark The Herald Angels Sing - Audionautix.mp3', 'Hip Hop Christmas - Twin Musicom.mp3', 'Jingle Bells - Kevin MacLeod.mp3', 'Jingle Bells 7 - Kevin MacLeod.mp3', 'Joy To The World - Audionautix.mp3', 'Noel - Audionautix.mp3', 'We Wish You a Merry Christmas - Twin Musicom.mp3', 'We Wish You A Merry Xmas - Audionautix.mp3']


def random_music():
    return random.choice(music_files)


@views.route('/')
def home():
    return render_template('home.html', music=random_music())


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
        return render_template(f'days/{day}.html')


@views.route('day/<request_day>')
def day(request_day: str):
    request_day = int(request_day)
    day = int(time.strftime('%d'))
    month = int(time.strftime('%m'))
    hour = int(time.strftime('%H'))
    year = int(time.strftime('%Y'))

    # REMOVE/COMMENT THIS LINE IN PRODUCTION
    return render_template(f'days/{request_day}.html', day=request_day)

    if month != 12 and year == 2021:
        return render_template('early.html')
    elif year > 2021 or (day > 24 and month == 12) or (request_day > day and month == 12) or (request_day == day and month == 12 and hour >= 6):
        return render_template(f'days/{request_day}.html', day=request_day)


@views.route('/credits')
def credits():
    return render_template('credits.html')
