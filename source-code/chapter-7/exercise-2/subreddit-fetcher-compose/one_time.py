
from models import *


def create_tables():
    db.connect()
    db.create_tables([Source, Request, Message], True)
    db.close()

if __name__ == '__main__':
    create_tables()
