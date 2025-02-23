import responses
import requests

from website.models import User, Lesson
from website import db
 
def test_signup(client, app):
    client.post("/sign-up", data={"email": "asd@asd", "firstName": "matis", "password1": "12345678","password2": "12345678", })

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "asd@asd"
        assert User.query.first().first_name == "matis"
        assert User.query.first().password == "12345678"


def test_login(client, app):
    print('loggggiiiinnnn')
    # Create a test user
    with app.app_context():
        user = User(email="asd@asd", first_name="matis", password="12345678")
        db.session.add(user)
        db.session.commit()

    response = client.post("/login", data={"email": "asd@asd", "password": "12345678"})
    assert response.status_code == 302  # 302 means redirect


def test_create_lesson(client, app):
    # Create and login user
    client.post("/sign-up", data={"email": "asd@asd", "firstName": "matis", "password1": "12345678","password2": "12345678", })

    response = client.post("/create", data={
        "time": "10:00 AM",
        "date": "2023-10-10",
        "subject": "Math",
        "pupil": "John Doe",
        "place": "Room 101"
    })

    with app.app_context():
        assert Lesson.query.count() == 1
        assert Lesson.query.first().time == "10:00 AM"
        assert Lesson.query.first().date == "2023-10-10"
        assert Lesson.query.first().subject == "Math"
        assert Lesson.query.first().pupil == "John Doe"
        assert Lesson.query.first().place == "Room 101"

    assert response.status_code == 302

def test_delete_lesson(client, app):
    client.post("/sign-up", data={"email": "asd@asd", "firstName": "matis", "password1": "12345678","password2": "12345678", })
    
    #Create a lesson
    with app.app_context():
        lesson = Lesson(time="10:00 AM", date="2023-10-10", subject="Math", pupil="John Doe", place="Room 101", user_id=1)
        db.session.add(lesson)
        db.session.commit()
    
    client.post("/delete-lesson", json={"lessonId": 1})

    with app.app_context():
        assert Lesson.query.count() == 0    

