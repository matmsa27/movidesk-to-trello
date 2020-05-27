import requests

from requests.exceptions import Timeout


from config import (
    TRELLO_BASE_URL,
    TRELLO_CREATE_CARDS,
    TRELLO_ID_LIST,
    TRELLO_KEY,
    TRELLO_TOKEN
)


def payload_to_trello(data):

    payload = {
        "name": "{} - #{}".format(data.get("Subject"), data.get("Id")),
        "description": data.get("Actions")[0].get("Description"),
        "label": data.get("Status"),
        "ticket_id": data.get("Id")
    }

    return payload


def create_card(data):
    payload = payload_to_trello(data)
    url = "https://{}/{}".format(TRELLO_BASE_URL, TRELLO_CREATE_CARDS)

    params = {
        "key": TRELLO_KEY,
        "token": TRELLO_TOKEN,
        "idList": TRELLO_ID_LIST,
        "name": payload.get("name")
    }
    try:
        response = requests.post(url=url, params=params, timeout=20)
    except Timeout:
        response = requests.post(url=url, params=params, timeout=30)
    return response
