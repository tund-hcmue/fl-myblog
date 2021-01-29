from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user ={'username': 'Tund'}
    posts = [
        {
            'author': {'username': 'Nguyen'},
            'body': 'Flask that la de hoc...'
        },
        {
            'suthor': {'username': Long},
            'body': 'Lap tring web voi Flask...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)