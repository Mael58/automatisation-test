from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to ze BEFE'

@app.route('/events')
def events():
    return render_template('events.html')