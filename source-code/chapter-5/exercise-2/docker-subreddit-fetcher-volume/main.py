from flask import Flask
from newsbot import *
from states import States

bot = Flask(__name__)


@bot.route('/index')
def index():
    return 'Thou shalt not pass!'


@bot.route('/telegram-update', methods=['POST'])
def telegram_update():
    handle_incoming_messages(States.last_updated_id)


if __name__ == '__main__':
    States.last_updated_id = get_last_updated()
    bot.run()


