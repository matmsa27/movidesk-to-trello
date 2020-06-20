from flask_api import status

from application.trello import (
    add_label_to_a_card,
    add_comment_on_card,
    create_card,
    get_cards_on_board,
)
from application.utils import (
    check_if_card_exists,
    make_card_description,
    make_card_name,
)


def receive_webhook_from_movidesk(request):
    if request.method == "POST":
        data = request.data

        # check if card exists
        card_name = make_card_name(data)
        cards_on_board_list = get_cards_on_board()

        card_checked = check_if_card_exists(card_name, cards_on_board_list)

        # if exists add comment
        if card_checked:
            description = make_card_description(data)
            comment_response = add_comment_on_card(card_checked, description)

            if comment_response.status_code == 200:
                return comment_response.json(), status.HTTP_200_OK
            else:
                return comment_response.json(), status.HTTP_400_BAD_REQUEST

        # if not existis follow the last logic

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
