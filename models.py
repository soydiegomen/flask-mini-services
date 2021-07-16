from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from app import db

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    notes = db.relationship("Note", backref='user')

    def __repr__(self):
        return '<User %r>' % self.username
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(users):
        usersArray = []
        for user in users:
            d = Serializer.serialize(user)
            usersArray.append(d)

        return usersArray

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.String(500), nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
    def serialize_list(notes):
        notesArray = []
        for note in notes:
            d = Serializer.serialize(note)
            notesArray.append(d)

        return notesArray

if __name__ == "__main__":

    # Run this file directly to create the database tables.
    #print 'Creating database tables...'
    db.create_all()
    #print "Done!"