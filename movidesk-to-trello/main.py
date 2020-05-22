# -*- coding: UTF-8 -*-

import json

from flask import Flask, request

from trello import create_card
from config import DEBUG

app = Flask(__name__)
app.debug = DEBUG  # Enable reloader and debugger


@app.route("/", methods=["POST"])
def receive_webhook_from_movidesk():
    if request.method == "POST":
        data = request.data
        response_trello = create_card(data)
        if response_trello.status_code == 200:
            return json.dumps(response_trello.text), 200, {'ContentType':'application/json'}
        return json.dumps(response_trello.text), 400, {'ContentType':'application/json'}


if __name__ == '__main__':  # Script executed directly (instead of via import)?
    app.run()  # Launch built-in web server and run this Flask webapp
