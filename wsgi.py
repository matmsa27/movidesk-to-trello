import os

from flask import request
from flask_api import FlaskAPI

from application.config import DEBUG
from application.app import receive_webhook_from_movidesk

app = FlaskAPI(__name__)


@app.route("/", methods=["POST"])
def home():
    return receive_webhook_from_movidesk(request)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
