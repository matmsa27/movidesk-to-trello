from flask_api import status

from application.trello import create_card


def receive_webhook_from_movidesk(request):
    if request.method == "POST":
        data = request.data

        response_trello = create_card(data)

        content = response_trello.json()

        if response_trello.status_code == 200:
            return content, status.HTTP_200_OK
        return content, status.HTTP_400_BAD_REQUEST
