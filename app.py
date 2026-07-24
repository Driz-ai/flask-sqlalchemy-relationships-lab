
from flask import Flask, jsonify, request

app = Flask(__name__)

events = []


class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title


@app.route("/")
def home():
    return jsonify({
        "message": "EventWise API"
    }), 200


@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([
        {
            "id": event.id,
            "title": event.title
        }
        for event in events
    ]), 200


@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({
            "error": "title is required"
        }), 400

    event = Event(
        id=len(events) + 1,
        title=data["title"]
    )

    events.append(event)

    return jsonify({
        "id": event.id,
        "title": event.title
    }), 201


if __name__ == "__main__":
    app.run(port=5555)