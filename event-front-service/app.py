from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config.update({"events": []})
global_id = 0

@app.route("/")
def index():
    return "Welcome to ze BEFE"


@app.route("/events")
def events():
    return render_template("events.html", events=app.config.get("events"))


@app.route("/event/<int:event_id>")
def event(event_id=None):
    result = list(
        filter(
            lambda event: event["event_id"] == int(event_id), app.config.get("events")
        )
    )
    return render_template("event.html", event=next(iter(result), None))


@app.route("/event", methods=["POST"])
def new_event():
    if 'event_title' not in request.form:
        return render_template('events.html', events=app.config.get("events"), error_msg='missing event title'), 400
    event_title = request.form["event_title"]
    event_is_free = 'is_free' in request.form
    global global_id
    global_id += 1
    event = {
        "event_id": global_id,
        "event_title": event_title,
        "is_free": event_is_free,
        "already_registered": False,
    }
    app.config.get('events').append(event)
    return redirect('/events')
