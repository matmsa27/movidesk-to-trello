from flask import request
from flask_api import FlaskAPI

from application.config import DEBUG
from application.app import receive_webhook_from_movidesk

app = FlaskAPI(__name__)


@app.route("/", methods=["POST"])
def home():
    return receive_webhook_from_movidesk(request)


if __name__ == '__main__':
    app.run(debug=DEBUG)
