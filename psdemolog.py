import logging

fmst_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmst_str, filename='error.log')



logging.debug('debug messages')
logging.info('confirmation notes')
logging.warning('warnings informations')
logging.error('an error notes')
logging.critical('panic error')