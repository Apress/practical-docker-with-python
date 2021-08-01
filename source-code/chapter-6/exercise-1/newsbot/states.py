import logging


class States(object):
    last_updated_id = ''

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s')

log = logging.getLogger('nbt')