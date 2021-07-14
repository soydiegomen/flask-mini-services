from flask import Flask
from app import app
from models import User
import json

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