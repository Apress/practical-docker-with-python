from states import States, log
from telegram import handle_incoming_messages
from models import *
from time import sleep

import sys
import pymysql


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
    log.info('Starting up')
    log.info('Waiting for 60 seconds for db to come up')
    sleep(60)
    
    log.info('Checking on dbs')
    try:
        db.connect()
    except OperationalError as o:
        print("Could not connect to db, please check db parameters")
        sys.exit(-1)
    except InternalError as e:
        # 1049 is MySQL error code for db doesn't exist - so we create it. 
        db_connection = pymysql.connect(host='mysql', user= 'root', password='dontusethisinprod')
        db_connection.cursor().execute('CREATE DATABASE newsbot')
        db_connection.close()
        db.create_tables([Source, Request, Message], True)

    try:
        States.last_updated = get_last_updated()
        while True:
            handle_incoming_messages(States.last_updated)
    except KeyboardInterrupt:
        log.info('Received KeybInterrupt, exiting')
