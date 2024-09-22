import base64
import os
from flask import Flask, request
import google.cloud.firestore


app = Flask(__name__)
dbname = os.environ['FIRESTORE_DB_NAME']
db = google.cloud.firestore.Client(database=dbname)

@app.route("/", methods=["POST"])
def index():
    """Receive and parse Pub/Sub messages."""
    envelope = request.get_json()
    if not envelope:
        msg = "no Pub/Sub message received"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    if not isinstance(envelope, dict) or "message" not in envelope:
        msg = "invalid Pub/Sub message format"
        print(f"error: {msg}")
        return f"Bad Request: {msg}", 400

    pubsub_message = envelope["message"]

    name = "World"
    if isinstance(pubsub_message, dict) and "data" in pubsub_message:
        name = base64.b64decode(pubsub_message["data"]).decode("utf-8").strip()

    print(f"Hello {name}!")

    results = db.collection('human').stream()
    data_list = [doc.to_dict() for doc in results]

    print(data_list)

    return ("", 204)