from time import sleep
from pslogconfig import logger

for item in range(1, 11):
    logger.debug(f'dummy log : {item}')
    sleep(.5)
