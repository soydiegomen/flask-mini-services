from flask import Flask
from app import app
from models import User
import json
from app import db

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
    print('#Creating user')
    admin = User(username='admin2', email='admin2@example.com')
    guest = User(username='guest2', email='guest2@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    return "<p>Creating user!</p>"