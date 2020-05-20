from states import States, log
from telegram import handle_incoming_messages


def get_last_updated():
    try:
        with open('last_updated.txt', 'r') as f:
            try:
                last_updated = int(f.read())
            except ValueError:
                last_updated = 0
        f.close()
    except FileNotFoundError:
        last_updated = 0
    log.debug('Last updated id: {0}'.format(last_updated))
    return last_updated

if __name__ == '__main__':

    try:
        log.debug('Starting up')
        States.last_updated = get_last_updated()
        while True:
            handle_incoming_messages(States.last_updated)
    except KeyboardInterrupt:
        log.info('Received KeybInterrupt, exiting')