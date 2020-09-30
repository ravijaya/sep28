"""log config"""

import logging

from logging.handlers import RotatingFileHandler

fmst_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmst_str)  # what?

fh = RotatingFileHandler('access.log', backupCount=5, maxBytes=64)
fh.setFormatter(fmt)

logger = logging.getLogger('thinkpad')
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)
