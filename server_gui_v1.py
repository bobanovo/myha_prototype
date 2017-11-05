from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect

import sqlite3

conn = sqlite3.connect('recdata1')
print ("Opened database successfully")
conn.close()

app= Flask (__name__)

@app.route('/')
def index():
    return render_template('first_gui.html')
    

@app.route('/list')
def list():
    con = sql.connect("recdata1")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from recdata1")

    rows = cur.fetchall(); 
    return render_template("first_gui.html",rows = rows)

if __name__=='__main__':
    app.run(debug=True)


