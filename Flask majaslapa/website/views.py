from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Lesson
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods =['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        lesson = request.form.get('lesson')

        if len(lesson) < 1:
            flash('Note is too short!', category='error')
        else:
            new_lesson = Lesson(data=lesson, user_id=current_user.id)
            db.session.add(new_lesson)
            db.session.commit()
            flash('Lesson added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/create', methods=['GET','POST'])
def create_lesson():
    if request.method == 'POST':
        time = request.form.get('time')
        print(var.type(time))

    return render_template("create.html", user=current_user)

@views.route('/delete-lesson', methods=['POST'])
def delete_lesson():
    lesson = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    lessonId = lesson['lessonId'] 
    lesson = Lesson.query.get(lessonId)
    if lesson:
        if lesson.user_id == current_user.id:
            db.session.delete(lesson)
            db.session.commit()

    return jsonify({})  