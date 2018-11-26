import logging


class States(object):
    last_updated_id = ''

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s')

log = logging.getLogger('nbt')