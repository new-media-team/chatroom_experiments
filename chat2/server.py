import eventlet
eventlet.monkey_patch()
import re
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit
import time, os
from flask import request

import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('connect')
def connect(methods=['GET', 'POST']):
    print("connected!")

replies = ["hello there", "how are you", "what's happening", "we're done here"]

state = {}

@socketio.on('input')
def myInput(event):
    print(" sending %s onwards ..." % event)
    print(request.sid)



    socketio.emit("output", event) # sends to everone
    #socketio.emit("output", event, include_self=False) # sends to everyone, except the browser that originated the event
    #emit("output", event) # send only to the browser that originated the event

    if (request.sid in state):
        state[request.sid] += 1
    else:
        state[request.sid] = 0
    print("STR IS")
    print(str(event))
    if (state[request.sid]<len(replies) and re.search("^{'message': 'command:", str(event))): # checks if the user is sending a command before bot responds
        time.sleep(2)
        print(state[request.sid], len(replies), replies)
        emit("output", dict(message=replies[state[request.sid]], username='bot'))

def check():
    while True:
        time.sleep(1)
        #socketio.emit("output", dict(message="hello from code", username="fake username"))

threading.Thread(target=check).start()

if __name__ == '__main__':
    socketio.run(app, debug=True,use_reloader=False,host='0.0.0.0' )
