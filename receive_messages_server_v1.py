import logging
import zmq
import sys
import click
import time

@click.command()
@click.option('-s', '--server', required=False, default='*', help='Server for listening (default is *')
@click.option('-p', '--port', required=False, default='6683', help='Port of server (default is 6683')
def listen(server, port):
    '''
    Receive message via ZeroMQ
    '''
    with zmq.Context() as context:
        with context.socket(zmq.PULL) as socket:
    
            socket.bind('tcp://%s:%s' % (server, port))
            click.echo('listening... on tcp://*:%s'  % port)
    
            while True:
                message = socket.recv_string()
                time.sleep (1) 
                click.echo(message)        
    

if __name__=="__main__":
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel('INFO')
    
    log.debug('Py is started...')
    log.debug('...version of python: ' + sys.version)
    
    listen()