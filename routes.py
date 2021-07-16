from flask import Flask
from app import app
from models import User, Note, Serializer
import json
from app import db
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

@app.route("/")
def hello_world():
    print('#Hello en consola 1.3')
    users = User.query.all()
    #lastUser = []
    #for user in users:
        #self.logger.info(f"{product.name} {product.price}")
        #self.logger.info(f"{comment.id} {comment.product.name}")
        #lastUser = user
        #print(f"{user.id} {user.username}")
    return json.dumps(User.serialize_list( users ) )


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
    #notes = Note.query.all()
    #engine = create_engine('mysql+mysqlconnector://root:root@localhost:8889/scrapy_test_db')
    #session = sessionmaker(bind=engine)
    #notes = session.query(Note).all()
    notes = db.session.query(Note).order_by(Note.id).all()
    #lastUser = []
    print('#Entro a get_note')
    result = []
    for note in notes:
        serializedNote = note.serialize()
        print(serializedNote)
        serializedUser = Serializer.serialize(serializedNote['user'])
        serializedNote['user'] = serializedUser

        result.append(serializedNote)
        print(serializedNote)
        #print(json.dumps(serializedNote))

    #return json.dumps(Note.serialize_list( notes ) )
    #return json.dumps(result)
    return "<p>Note!</p>"