"""
utils.py file for have methods and improve the
code organization and all logical
"""

import requests

from application.config import (
    MOVIDESK_TOKEN,
)

def make_card_name(data):
    name_card = "%s - #%s" % (data.get("Subject"), data.get("Id"))
    return name_card

def make_card_description(data):
    description = data.get("Actions")[0].get("Description")

    creator_id = get_creator_id_from_action(data)
    if creator_id:
        creator_profile = get_creator_profile_from_movidesk(creator_id).json()
        if creator_profile:
            creator_name = get_name_from_movidesk_json(creator_profile)
            creator_email = get_email_from_movidesk_json(creator_profile)

            description = "{} \n{} \n{} \n".format(description, creator_name, creator_email)

    return description

def get_creator_id_from_action(data):
    try:
        return data.get("Actions")[0].get("CreatedBy").get("Id")
    except (KeyError, IndexError):
        return None

def get_creator_profile_from_movidesk(creator_id):
    url = "https://api.movidesk.com/public/v1/persons"
    params = {
        "token": MOVIDESK_TOKEN,
        "id": creator_id
    }

    try:
        return requests.get(url=url, params=params, timeout=30)
    except:
        return None

def get_movidesk_ticket_info(ticket_id):

    url = "https://api.movidesk.com/public/v1/tickets"
    params = {
        "token": MOVIDESK_TOKEN,
        "id": ticket_id
    }
    try:
        return requests.get(url=url, params=params, timeout=30)
    except:
        return None

def get_name_from_movidesk_json(data):
    try:
        name = data.get('businessName')
        return name
    except (KeyError, IndexError):
        return ''


def get_email_from_movidesk_json(data):
    try:
        email = data.get('emails')[0].get('email')
        return email
    except (KeyError, IndexError):
        return ''


def check_if_card_exists(card_name_check, cards_on_board_list):

    for card in cards_on_board_list.json():
        if card["name"] == card_name_check:
            return card

