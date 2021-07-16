from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:8889/scrapy_test_db'
db = SQLAlchemy(app)

""" @app.route("/")
def hello_world():
    return "<p>Hello, World 2.0!</p>" """

if __name__ == "__main__":

    # We need to make sure Flask knows about its views before we run
    # the app, so we import them. We could do it earlier, but there's
    # a risk that we may run into circular dependencies, so we do it at the
    # last minute here.

    from routes import *

    app.run(debug=True)
