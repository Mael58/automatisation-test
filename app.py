from flask import Flask, render_template

app = Flask(__name__)

app.config.update({
    "events": [
    ]
})


@app.route("/")
def index():
    return "Welcome to ze BEFE"


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/event/<int:event_id>")
def event(event_id=None):
    result = list(
        filter(lambda event: event["event_id"] == int(event_id), app.config.get("events"))
    )
    return render_template("event.html", event=next(iter(result), None))
