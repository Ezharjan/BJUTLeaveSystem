
import os
import sys
import time
import uuid
import traceback


from gevent.pywsgi import WSGIServer
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



@app.route('/')
def hello_flask():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.debug = False
    host= '0.0.0.0'
    port = 5000
    if app.debug:
        app.run(host, int(port))
    else:
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()


