from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'monkey'
#images = Images(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'


@app.route('/')
def home():
    return render_template('home.html')
@app.route('/signedIn')
def home2():
    return 'home2.html'


db = SQLAlchemy(app)
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    genre = db.Column(db.String(30), nullable=False)
    book_rating = db.Column(db.Integer, nullable=False, default = 'N/A')
    publisher = db.Column(db.String(30), nullable=False, default = 'N/A')
    comments = db.Column(db.String(30), nullable=False, default = 'N/A')
    date_published = db.Column(db.DateTime, nullable=False)

db.create_all()


def __repr__(self):
    return 'Blog post ' + str(self.id)



if __name__ == '__main__':
    app.run(debug=True)