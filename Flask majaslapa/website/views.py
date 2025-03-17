from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Lesson
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/home', methods =['GET','POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/create', methods=['GET','POST'])
@login_required
def create_lesson():
    if request.method == 'POST':
        time = request.form.get('time')
        date = request.form.get('date')
        subject = request.form.get('subject')
        pupil = request.form.get('pupil')
        place = request.form.get('place')
        if len(time) < 1:
            flash('You have to choose a time!', category='error')
        elif len(date) < 1:
            flash('You have to choose a date!', category='error')
        elif len(subject) > 200:
            flash('The name of subject is too long!', category='error')
        elif len(pupil) > 200:
            flash('The name of pupil is too long!', category='error')
        elif len(place) > 200:
            flash('The name of place is too long!', category='error')
        else:
            new_lesson = Lesson(time=time, date=date, subject=subject, pupil=pupil, place=place, user_id=current_user.id)
            db.session.add(new_lesson)
            db.session.commit()
            flash('Lesson added!', category='success')
            return redirect(url_for('views.home'))

    return render_template("create.html", user=current_user)

@views.route('/delete-lesson', methods=['POST'])
def delete_lesson():
    lesson = json.loads(request.data)
    lessonId = lesson['lessonId'] 
    lesson = Lesson.query.get(lessonId)
    if lesson:
        if lesson.user_id == current_user.id:
            db.session.delete(lesson)
            db.session.commit()

    return jsonify({})  