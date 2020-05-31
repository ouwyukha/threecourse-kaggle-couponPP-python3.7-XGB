"""
    This file has a utility function for logging.
"""

import logging

def get_logger():
    logger = logging.getLogger('my_logger')

    if len(logger.handlers) == 0:
        logger.setLevel(logging.DEBUG)
        
        fh = logging.FileHandler('../model/log.txt')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)-15s %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        
        logger.addHandler(ch)
        logger.addHandler(fh)
    
    return logger

