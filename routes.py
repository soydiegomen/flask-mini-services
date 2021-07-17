from flask import Flask, jsonify, request
from app import app
from models import User, Note
from app import db


@app.route("/")
def index():
    return "<p>Hello!</p>"

@app.route("/users")
def get_users():
    email = request.args.get('email')
    print(f'#Input {email}')
    #users = User.query.filter(User.email == email).all()
    search = f'%{email}%'
    users = User.query.filter(User.email.like(search)).all()
    return jsonify(users)


@app.route("/create_user")
def create_user():
    admin = User(username='admin3', email='admin3@example.com')
    guest = User(username='guest3', email='guest3@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return jsonify({})

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
    notes = Note.query.all()

    return jsonify(notes)