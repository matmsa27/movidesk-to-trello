import os
import sentry_sdk

from flask import request
from flask_api import FlaskAPI

from decouple import config
from sentry_sdk.integrations.flask import FlaskIntegration

from application.config import DEBUG
from application.app import receive_webhook_from_movidesk


sentry_sdk.init(
    dsn=config("SENTRY_DSN"),
    integrations=[FlaskIntegration()]
)


app = FlaskAPI(__name__)


@app.route("/", methods=["POST"])
def home():
    return receive_webhook_from_movidesk(request)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
