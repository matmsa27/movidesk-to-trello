from flask import request
from flask_api import FlaskAPI, status

from trello import create_card
from config import DEBUG

app = FlaskAPI(__name__)


@app.route("/", methods=["POST"])
def receive_webhook_from_movidesk():
    if request.method == "POST":
        data = request.data

        response_trello = create_card(data)

        content = response_trello.json()

        if response_trello.status_code == 200:
            return content, status.HTTP_200_OK
        return content, status.HTTP_400_BAD_REQUEST


if __name__ == '__main__':
    app.run(debug=DEBUG)
