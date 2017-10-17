
import socket
import sys
import bokeh
import logging
import zmq




if __name__=="__main__":
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel('INFO')
    log.info('Program starting')
    log.info('version of python: ' + sys.version)


