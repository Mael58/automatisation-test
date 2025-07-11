from flask import Flask, render_template, request, redirect
import grpc
import sys
import os

sys.path.insert(0, os.path.basename(os.path.curdir))
from models.payment_pb2_grpc import PaymentStub
from models.payment_pb2 import PayRequest, PayReply

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
    return render_template("event.html", event=find_event(event_id))


@app.route("/event", methods=["POST"])
def new_event():
    if 'event_title' not in request.form:
        return render_template('events.html', events=app.config.get("events"), error_msg='missing event title'), 400
    event_title = request.form['event_title']
    event_is_free = 'is_free' in request.form
    if event_is_free:
        price = 0
    else:
        price = request.form['price']
    global global_id
    global_id += 1
    event = {
        "event_id": global_id,
        "event_title": event_title,
        "is_free": event_is_free,
        "already_registered": False,
        "price": price
    }
    app.config.get('events').append(event)
    return redirect('/events')

@app.route('/event/<int:event_id>/subscribe', methods=["POST"])
def subscribe(event_id=None):
    event = find_event(event_id)
    amount = float(event['price'])
    user_id = int(request.form['user_id'])
    card_number = int(request.form['card_id'])
    error_msg = None
    if event and not event['is_free']:
        response = None
        with grpc.insecure_channel("localhost:50051") as channel:
            stub = PaymentStub(channel)
            pay_request = PayRequest(
                amount=amount,
                card_number=card_number,
                event_id=event_id,
                user_id=user_id
            )
            response = stub.Pay(pay_request)
        if response is None or response and not response.status:
            error_msg = 'Payment refused'
        return render_template('event.html', event=event, error_msg=error_msg)
    if event and event['is_free']:
        print('register')
        return redirect('/events')


def find_event(event_id):
    result = list(
        filter(
            lambda event: event["event_id"] == int(event_id), app.config.get("events")
        )
    )
    return next(iter(result), None)