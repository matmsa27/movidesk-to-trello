from flask_api import status

from application.config import (
    MOVIDESK_TOKEN,
)

from application.trello import (
    add_label_to_a_card,
    add_comment_on_card,
    create_card,
    get_cards_on_board,
    add_due_date_on_card
)
from application.utils import (
    check_if_card_exists,
    make_card_description,
    make_card_name,
    get_movidesk_ticket_info
)


def check_card_logical_view(data, due_date):
    '''
    Method to logical on check if card already exists on board
    '''

    # Get card name and and get all cards on board
    card_name = make_card_name(data)
    cards_on_board_list = get_cards_on_board()

    # Call the method to verify if the card already exists on board
    card_checked = check_if_card_exists(card_name, cards_on_board_list)

    if card_checked:
        # If card exists, the request will insert a comment on card
        description = make_card_description(data)
        comment_response = add_comment_on_card(card_checked["id"], description)
        if due_date:
            add_due_date_on_card(card_checked["id"], due_date)            

        if comment_response.status_code == 200:
            return comment_response.json(), status.HTTP_200_OK
        else:
            return comment_response.json(), status.HTTP_400_BAD_REQUEST
    
    return False


def add_label_logical_view(data, response_trello):
    '''
    Method to logical to add label on card created
    '''

    # Get the id from card created
    card_created_id = response_trello.json().get("id")

    # Call the method to add label on card
    add_label_response = add_label_to_a_card(card_created_id, data)

    if add_label_response.status_code == 200:
        return add_label_response.json(), status.HTTP_200_OK
    else:
        return add_label_response.json(), status.HTTP_400_BAD_REQUEST


def receive_webhook_from_movidesk(request):
    '''
    The view responsible to receive request from movidesk
    '''
    if request.method == "POST":
        data = request.data
        '''
        Call the method to responsible to validate logic if card exists
        If checked, the request returns the response for insert a comment
        If not exists, will create a new card, and after that add the label
        '''
        due_date = get_movidesk_ticket_info(data.get("Id")).json().get("slaSolutionDate")
        if due_date:
            due_date = due_date + '.000Z'

        checked = check_card_logical_view(data, due_date)

        if checked:
            return checked
        
        else:
            response_trello = create_card(data, due_date)

            if response_trello.status_code == 200:
                return add_label_logical_view(data, response_trello)
            else:
                return response_trello.json(), status.HTTP_400_BAD_REQUEST
