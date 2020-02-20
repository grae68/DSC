from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/events')
def events():
    return render_template('events.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')