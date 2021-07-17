from flask import Flask, jsonify
from app import app
from models import User, Note, Serializer
import json
from app import db
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker, joinedload, noload
from sqlalchemy import create_engine


@app.route("/")
def index():
    return "<p>Hello!</p>"

@app.route("/users")
def get_users():
    print('#Hello en consola 1.3')
    users = User.query.all()
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