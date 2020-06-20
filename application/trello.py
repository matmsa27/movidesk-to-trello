import requests

from requests.exceptions import Timeout

from application.config import (
    TRELLO_BASE_URL,
    TRELLO_BOARD_ID,
    TRELLO_CARDS,
    TRELLO_ID_LIST,
    TRELLO_KEY,
    TRELLO_TOKEN,
    TRELLO_ID_LABEL_N3,
    TRELLO_ID_LABEL_SERVICES,
)
from application.utils import (
    make_card_description,
    make_card_name,
)


def params_auth_trello():
    params = dict(
        key=TRELLO_KEY,
        token=TRELLO_TOKEN
    )
    return params


def payload_to_trello(data):

    payload = {
        "name": make_card_name(data),
        "description": make_card_description(data),
        "label": data.get("Status"),
        "ticket_id": data.get("Id")
    }

    return payload


def create_card(data):
    payload = payload_to_trello(data)
    url = "https://%s/%s" % (TRELLO_BASE_URL, TRELLO_CARDS)

    params = params_auth_trello()
    params["idList"] = TRELLO_ID_LIST
    params["name"] = payload.get("name"),
    params["desc"] = payload.get("description")

    try:
        response = requests.post(url=url, params=params, timeout=20)
    except Timeout:
        response = requests.post(url=url, params=params, timeout=30)
    return response


def get_cards_on_board():
    url = "https://%s//1/boards/%s/cards" % (
        TRELLO_BASE_URL, TRELLO_BOARD_ID)
    
    params = params_auth_trello()

    try:
        response = requests.get(url=url, params=params, timeout=20)
    except Timeout:
        response = requests.get(url=url, params=params, timeout=30)
    return response


def add_comment_on_card(card_id, comment_text):
    url = "https://%s/%s/%s/actions/comments" % (
        TRELLO_BASE_URL, TRELLO_CARDS, card_id)
    
    params = params_auth_trello()
    params["text"] = comment_text

    try:
        response = requests.post(url=url, params=params, timeout=20)
    except Timeout:
        response = requests.post(url=url, params=params, timeout=30)
    return response


def add_label_to_a_card(card_id, data):
    url = "https://%s/%s/%s/idLabels" % (
        TRELLO_BASE_URL, TRELLO_CARDS, card_id)

    card_type = data["CustomFieldValues"][0]["Items"][0]["CustomFieldItem"]
    card_type = card_type.lower().strip()

    params = params_auth_trello()

    if card_type == "plataforma":
        params["value"] = TRELLO_ID_LABEL_SERVICES
        response = requests.post(url=url, params=params, timeout=20)
    else:
        params["value"] = TRELLO_ID_LABEL_N3
        response = requests.post(url=url, params=params, timeout=30)
    return response
