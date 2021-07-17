from flask import Flask, jsonify
from app import app
from models import User, Note, Serializer
import json
from app import db
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker, joinedload, noload
from sqlalchemy import create_engine

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder

@app.route("/")
def hello_world():
    print('#Hello en consola 1.3')
    users = User.query.all()
    #lastUser = []
    for user in users:
        #self.logger.info(f"{product.name} {product.price}")
        #self.logger.info(f"{comment.id} {comment.product.name}")
        #lastUser = user
        #print(f"{user.id} {user.username}")
        print(user)
    #return json.dumps(User.serialize_list( users ) )
    return jsonify(users)


@app.route("/create_user")
def create_user():
    admin = User(username='admin2', email='admin2@example.com')
    guest = User(username='guest2', email='guest2@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return "<p>Users created!</p>"

@app.route("/create_note")
def create_notes():
    noteOne = Note(title='First note', content='Note details ...', product_id=1)
    noteTwo = Note(title='Seconde note', content='Two note details ...', product_id=2)
    db.session.add(noteOne)
    db.session.add(noteTwo)
    db.session.commit()
    return "<p>Notes created!</p>"

@app.route("/notes")
def get_notes():
    notes = Note.query.all()

    #jsonNotes = json.dumps(notes, cls=new_alchemy_encoder(), check_circular=True)
    #jsonNotes = json.dumps(notes, cls=AlchemyEncoder)

    #print(jsonNotes)
    #return jsonNotes
    return jsonify(notes)