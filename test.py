import logging

logging.basicConfig(filename='console', encoding='etf-8',
                    filemode='w', level=logging.DEBUG)

logging.debug('DEBUG')
logging.debug('INFO')
logging.debug('WARNING')
logging.debug('ERROR')
logging.debug('CRITICAL')
