from flask import Flask, render_template
from pathlib import Path

import json
import sqlite3

app = Flask(__name__)

def file_exists(file_name: str):
    return False

DB_LOCATION = "/home/pi/projects/fartbot/fartstreak.db"

@app.route("/")
def main():
    res = None # pre-define for scope

    # used for people testing without sqlite DB
    if file_exists(DB_LOCATION) == True:
        cur = sqlite3.connect(DB_LOCATION).cursor()
        res = cur.execute('SELECT * FROM fartstreak').fetchall()

        #print(type(out))
        #print(type(rend))
    else:
        # example.json should always exist
        f = open("example.json")
        res = json.load(f)

    # sort based on longest streak
    rend = sorted(res, key=lambda x: x[5])
    out = rend[::-1]

    # see README for 'out' json format
    return render_template("main.html", Database = out)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5001, url_scheme='https')
    #app.run( host='0.0.0.0', port=80)
