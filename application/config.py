'''
File created to define the FIXED Variables
'''

from decouple import config

'''
Debugging mode from project
'''
DEBUG = config("DEBUG", default=True, cast=bool)

'''
Variables for Trello API
'''
TRELLO_BASE_URL = "api.trello.com"
TRELLO_CARDS = "1/cards"
TRELLO_KEY = config("TRELLO_KEY")
TRELLO_BOARD_ID = config("TRELLO_BOARD_ID")
TRELLO_ID_LIST = config("TRELLO_ID_LIST")
TRELLO_TOKEN = config("TRELLO_TOKEN")
TRELLO_ID_LABEL_N3 = config("TRELLO_ID_LABEL_N3")
TRELLO_ID_LABEL_SERVICES = config("TRELLO_ID_LABEL_SERVICES")
TRELLO_ID_LABEL_TRIAGE = config("TRELLO_ID_LABEL_TRIAGE") 
