import requests

from requests.exceptions import Timeout


from application.config import (
    TRELLO_BASE_URL,
    TRELLO_CARDS,
    TRELLO_ID_LIST,
    TRELLO_KEY,
    TRELLO_TOKEN,
    TRELLO_ID_LABEL_N3,
    TRELLO_ID_LABEL_SERVICES
)


def params_auth_trello():
    params = dict(
        key=TRELLO_KEY,
        token=TRELLO_TOKEN
    )
    return params


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
    url = "https://{}/{}".format(TRELLO_BASE_URL, TRELLO_CARDS)

    params = params_auth_trello()
    params["idList"] = TRELLO_ID_LIST
    params["name"] = payload.get("name"),
    params["desc"] = payload.get("description")

    try:
        response = requests.post(url=url, params=params, timeout=20)
    except Timeout:
        response = requests.post(url=url, params=params, timeout=30)
    return response


def add_label_to_a_card(card_id, data):
    url = "https://{}/{}/{}/idLabels".format(TRELLO_BASE_URL, TRELLO_CARDS, card_id)
    
    card_type = data["CustomFieldValues"][0]["Items"][0]["CustomFieldItem"]
    card_type = card_type.lower().strip()

    params = params_auth_trello()

    if card_type == "plataforma":  
        params["value"] = TRELLO_ID_LABEL_SERVICES
        response = requests.post(url=url, params=params, timeout=20)
    else:
        params["value"] = TRELLO_ID_LABEL_N3
        response = requests.post(url=url, params=params, timeout=20)
    return response
