from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1111@localhost:3306/my_db'
db.init_app(app)


# @app.before_request
# def before_request():
#     db.create_all()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
