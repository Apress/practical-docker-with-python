import re
from time import sleep
import requests

from states import States, log
from constants import *
from reddit import get_latest_news
from models import *
import peewee

__author__ = 'Sathyajith'



def get_updates(last_updated):
    log.debug('Checking for requests, last updated passed is: {}'.format(last_updated))
    sleep(UPDATE_PERIOD)
    response = requests.get(API_BASE + BOT_KEY + '/getUpdates', params={'offset': last_updated+1})
    json_response = FALSE_RESPONSE
    if response.status_code != 200:
        # wait for a bit, try again
        sleep(UPDATE_PERIOD*20)
        get_updates(last_updated)
    try:
        json_response = response.json()
    except ValueError:
        sleep(UPDATE_PERIOD*20)
        get_updates(last_updated)
    log.info('received response: {}'.format(json_response))
    return json_response


def post_message(chat_id, text):
    log.info('posting {} to {}'.format(text, chat_id))
    payload = {'chat_id': chat_id, 'text': text}
    requests.post(API_BASE + BOT_KEY + '/sendMessage', data=payload)


def handle_incoming_messages(last_updated):
    r = get_updates(last_updated)
    split_chat_text = []
    if r['ok']:
        for req in r['result']:
            chat_sender_id = req['message']['chat']['id']
            try:
                chat_text = req['message']['text']
                split_chat_text = chat_text.split()
            except KeyError:
                chat_text = ''
                split_chat_text.append(chat_text)
                log.debug('Looks like no chat text was detected... moving on')
            try:
                person_id = req['message']['from']['id']
            except KeyError:
                pass

            log.info('Chat text received: {0}'.format(chat_text))
            r = re.search('(source+)(.*)', chat_text)

            if (r is not None and r.group(1) == 'source'):
                if r.group(2):
                    sources_dict[person_id] = r.group(2)
                    log.info('Sources set for {0} to {1}'.format(person_id, sources_dict[person_id]))
                    with db.atomic() as txn:
                        try:
                            sources = Source.create(person_id=person_id, fetch_from=sources_dict[person_id])
                            log.info('Inserted row id: {0}'.format(sources.person_id))
                        except peewee.IntegrityError:
                            sources = Source.update(fetch_from=sources_dict[person_id]).where(person_id == person_id)
                            rows_updated = sources.execute()
                            log.info('Updated {0} rows, query obj {1}'.format(rows_updated, sources))
                        txn.commit()

                    post_message(person_id, 'Sources set as {0}!'.format(r.group(2)))
                else:
                    post_message(person_id, 'We need a comma separated list of subreddits! No subreddit, no news :-(')
            if chat_text == '/stop':
                log.debug('Added {0} to skip list'.format(chat_sender_id))
                skip_list.append(chat_sender_id)
                post_message(chat_sender_id, "Ok, we won't send you any more messages.")

            if chat_text in ('/start', '/help'):
                helptext = '''
                    Hi! This is a News Bot which fetches news from subreddits. Use "/source" to select a subreddit source.
                    Example "/source programming,games" fetches news from r/programming, r/games.
                    Use "/fetch for the bot to go ahead and fetch the news. At the moment, bot will fetch total of 5 posts from all sub reddits
                    I will have this configurable soon.
                '''
                post_message(chat_sender_id, helptext)

            if split_chat_text[0] == '/fetch' and (person_id not in skip_list):
                post_message(person_id, 'Hang on, fetching your news..')
                try:
                    sub_reddits = Source.get(person_id = person_id).fetch_from.strip()
                    summarized_news = get_latest_news(sub_reddits)
                    post_message(person_id, summarized_news)
                except peewee.DoesNotExist:
                    post_message(person_id, 'Could not find a saved subreddit, please try setting sources with /source')
                    
            last_updated = req['update_id']
            with open('last_updated.txt', 'w') as f:
                f.write(str(last_updated))
                States.last_updated = last_updated
                log.debug(
                    'Updated last_updated to {0}'.format(last_updated))
            f.close()
