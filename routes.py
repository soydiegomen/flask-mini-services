from flask import jsonify, request
from app import app
from models import User, Note
from app import db
from sqlalchemy import or_


@app.route("/")
def index():
    return "<p>Hello!</p>"

@app.route("/users", methods=['GET'])
def get_users():
    email = request.args.get('email')
    query = User.query

    if email :
        search = f'%{email}%'
        query = query.filter(or_ (
            User.email.like(search),
            User.username.like(search)
        ))

    users = query.all()

    return jsonify(users)


@app.route("/create_user")
def create_user():
    admin = User(username='admin3', email='admin3@example.com')
    guest = User(username='guest3', email='guest3@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return jsonify({})

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    print(data)
    print('#Email ' + data['email'])
    user.email = data['email']
    db.session.commit()
    return jsonify(user)
    

@app.route("/create_note")
def create_notes():
    noteOne = Note(title='First note', content='Note details ...', user_id=7)
    noteTwo = Note(title='Seconde note', content='Two note details ...', user_id=7)
    db.session.add(noteOne)
    db.session.add(noteTwo)
    db.session.commit()
    return jsonify({})

@app.route("/notes")
def get_notes():
    user_email = request.args.get('user_email')
    print(f'#Input {user_email}')
    search = f'%{user_email}%'
    notes = Note.query.filter(Note.user.has(User.email.like(search))).all()

    return jsonify(notes)