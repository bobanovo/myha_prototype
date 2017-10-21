import logging
import zmq
import sys
import click
import time


@click.command()
@click.option('-m', '--message', required=True, help='Text of message')
@click.option('-s', '--server', required=False, default='127.0.0.1', help='IP address of server (default is 127.0.0.1')
@click.option('-p', '--port', required=False, default='6683', help='Port of server (default is 6683)')
@click.option('-t', '--timeout', required=False, default=3000, help='Timeout in ms (default is 3s')
@click.option('--echo', is_flag=True, help='Only echo')
def send(message,server,port,echo,timeout):
    '''
    Send message to server via ZeroMQ
    '''
    serveradd = 'tcp://' + server + ":" + port
    if echo==True:
        click.echo(serveradd + " ::: " + message)
    else:
        click.echo('SEND massage ' + message + ' to ' + serveradd)
        if click.confirm('Do you want to continue?',default=True):
            with zmq.Context() as context:
                context.setsockopt(zmq.LINGER, timeout)
                with context.socket(zmq.PUSH) as socket:
                    socket.connect(serveradd)
                    socket.send_string(message,zmq.NOBLOCK) # pro timeout, ale nefunguje
                
            

if __name__=="__main__":
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel('DEBUG')
    
    log.debug('Py is started...')
    log.debug('...version of python: ' + sys.version)
    
    send()