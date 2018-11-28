__author__ = 'Sathyajith'

from os import environ
ERR_NO_SOURCE = 'No sources defined! Set a source using /source list, of, sub, reddits'
skip_list = []
sources_dict = {}

BOT_KEY = environ.get('NBT_ACCESS_TOKEN')
REDDIT_CLIENT_ID = environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = environ.get('REDDIT_CLIENT_SECRET')
API_BASE = 'https://api.telegram.org/bot'
UPDATE_PERIOD = 6
FALSE_RESPONSE = {"ok": False}
