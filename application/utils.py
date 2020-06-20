"""
utils.py file for have methods and improve the
code organization and all logical
"""


def make_card_name(data):
    name_card = "%s - #%s" % (data.get("Subject"), data.get("Id"))
    return name_card


def make_card_description(data):
    description_card = data.get("Actions")[0].get("Description")
    return description_card


def check_if_card_exists(card_name_check, cards_on_board_list):

    for card in cards_on_board_list.json():
        if card["name"] == card_name_check:
            return card["id"]

