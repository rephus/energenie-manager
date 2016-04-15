#!/usr/bin/python
import time
from flask import Flask, jsonify,Response, render_template, request #http://flask.pocoo.org/
import json
import ConfigParser
import os.path
from energenie import switch_on, switch_off


#config = ConfigParser.ConfigParser()
#config.read("config.cfg")
#nmap_enabled = config.getboolean('network','nmap_enabled')

app = Flask(__name__)

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route("/")
def index():
    #how to server static files http://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask
    #return render_template('index.html')
    content = get_file('templates/index.html')
    return Response(content, mimetype="text/html")

@app.route("/sockets")
def sockets():
    sockets = [
        { "id": 1 ,
            "name": "socket 1",
            "status": True
        },
        { "id": 2,
            "name": "socket 2",
            "status": True
        },
        { "id": 3 ,
            "name": "socket 3",
            "status": True
        },
        { "id": 4,
            "name": "socket 4",
            "status": True
        }
    ];
    return jsonify({"sockets": sockets});

@app.route("/switch")
def switch():
    socket = int(request.args.get('socket', ''))
    status = request.args.get('status', '')

    print("Change socket {} to {}".format(socket, status))

    if status == "true":
        print("Switch on ", socket)
        switch_on(socket)
    else:
        print("Switch off ", socket)
        switch_off(socket)

    return jsonify({"socket": socket, "status": status})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug = True)
