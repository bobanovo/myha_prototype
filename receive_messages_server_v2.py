import logging
import zmq
import sys
import click
import time
import sqlite3 as db

# main listener
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
    
# store received data
# message as: "/A/B/C" as object;"qwertz" as data;"date-time" as datetime
# object - first part of message
# data - second part of message 
def storedata(database, table, record):
    '''
    Store data into storage - as DB - sqlite (table recdata1)
    '''
    
    try:
        dbcon = db.connect(database)
        with dbcon:
            dbcur = dbcon.cursor()    
            dbcur.execute('INSET INTO %s VALUES ()' % table) #change to insert data
            dbcur.executemany("INSERT INTO recdata VALUES(?, ?, ?)", data) # data is list of list ((A,B,C),(AA,BB,CC),...)
        
        data = dbcur.fetchone()
            
        log.debug ("SQLite version: %s" % data)
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)    
    finally:
        if dbcon:
            dbcon.close()    
    

# ----------------------------------------------------------------
if __name__=="__main__":
    logging.basicConfig()
    log = logging.getLogger(__name__)
    log.setLevel('DEBUG')
    
    log.debug('Py is started...')
    log.debug('Version of python: ' + sys.version)
    
    try:
        dbcon = db.connect('recdata1')
        dbcur = dbcon.cursor()    
        dbcur.execute('SELECT SQLITE_VERSION()')
            
        data = dbcur.fetchone()
            
        log.debug ("SQLite version: %s" % data)
    except lite.Error as e:
        print("Error %s:" % e.args[0])
        sys.exit(1)    
    finally:
        if dbcon:
            dbcon.close()    
    
    listen()