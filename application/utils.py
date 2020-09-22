"""
utils.py file for have methods and improve the
code organization and all logical
"""


def make_card_name(data):
    name_card = "%s - #%s" % (data.get("body").get("Subject"), data.get("body").get("Id"))
    return name_card


def make_card_description(data):
    description = data.get("body").get("Actions")[0].get("Description")
    # name = get_name_from_movidesk_json(data)
    # email = get_email_from_movidesk_json(data)

    # description = "{} \n {} \n {} \n".format(description_card, name, email)

    return description


def get_name_from_movidesk_json(data):
    try:
        name = data.get("Actions")[0].get("Attachments")[0].get("CreatedBy").get("BusinessName")
        return name
    except (KeyError, IndexError):
        return ''


def get_email_from_movidesk_json(data):
    try:
        email = data.get("Actions")[0].get("Attachments")[0].get("CreatedBy").get("Email")
        return email
    except (KeyError, IndexError):
        return ''


def check_if_card_exists(card_name_check, cards_on_board_list):

    for card in cards_on_board_list.json():
        if card["name"] == card_name_check:
            return card["id"]

