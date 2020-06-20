from flask_api import status

from application.trello import create_card, add_label_to_a_card


def receive_webhook_from_movidesk(request):
    if request.method == "POST":
        data = request.data

        response_trello = create_card(data)

        card_content = response_trello.json()

        if response_trello.status_code == 200:
            card_created_id = card_content.get("id")

            add_label_response = add_label_to_a_card(card_created_id, data)
            label_content = add_label_response.json()

            if add_label_response.status_code == 200:
                return label_content, status.HTTP_200_OK
            else:
                return label_content, status.HTTP_400_BAD_REQUEST

        return card_content, status.HTTP_400_BAD_REQUEST
