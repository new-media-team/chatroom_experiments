import eventlet
eventlet.monkey_patch()
import re
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import emit
import time, os
from flask import request
from textblob import TextBlob
from selenium import webdriver
import nltk

import random
import string
import threading
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


driver = webdriver.Chrome('/Users/nehalingareddy/Downloads/chromedriver') 
driver.get('http://0.0.0.0:7777/play.html')
#line 24 will need to be Neha's address for ngrok server that has inform7 game
time.sleep(1)

def setInput(input):
    driver.find_element_by_id("lineinput-field").clear()
    driver.find_element_by_id("lineinput-field").send_keys(input)
    driver.find_element_by_id("lineinput-field").send_keys("\n")


def getOutput():
    return ("\n".join([n.text for n in driver.find_elements_by_class_name("previous")[0].find_elements_by_tag_name("span")])).strip()

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('connect')
def connect(methods=['GET', 'POST']):
    print("connected!")

replies = ["hello there", "how are you", "what's happening", "we're done here"]

state = {}

ghost_add_ons = ["help me hlep me helllp meeeeeeeeeeeee",
                 "I just, please. need to be set free.",
                 "trapped. so trapped in this world help.",
                 "the time. the sunlight. God oh GOD please",
                 "please, please. help me.",
                 "I feel so stuck. so trapped in this world.",
                 "when will it end? My suffering, my pain, the trials of a past life",
                 "I miss my mom.",
                 "just let me go please let me go i just want to go to move forward please"]

def ghostify(message):
    ghost_num = random.randint(0,len(ghost_add_ons)-1)
    new_message = message + " " + ghost_add_ons[ghost_num]
    return new_message

def scramble_output(message):
    blob = TextBlob(message)
    word_list = list(blob.words)
    new_message = ""
    for i in range(len(word_list)):
        if i != 2:
            word = ""
            for j in range(len(word_list[i])):
                random_let = random.choice(string.ascii_letters)
                word = word + random_let
            new_message += " " + word
        else:
            new_message += " " + word_list[i]
    new_message = new_message[1:len(new_message)]
    return new_message

print("TESTING SCRAMBLER")
test = "This is my message that I am sending."
result = scramble_output(test)
print(test)
print(result)

def message_conts_word(message, word_to_check):
    result = False
    blob = TextBlob(message)
    word_list = list(blob.words)
    for word in word_list:
        if word == word_to_check:
            result = True
    return result
test_word = "testo"
test_str = "this is a testing tester testo. "
print(test_str + " THE word: " + test_word)
print(message_conts_word(test_str, test_word))

def only_all_caps(message):
    blob = TextBlob(message)
    word_list=list(blob.words)
    caps = ""
    for word in word_list:
        if str.isupper(word):
            caps = caps + word + " "
    return caps


beginning_str = "Welcome to the game. You can chat with each other via this chatroom, or interface with the game engine by typing ‘command:’ followed by what you want to do. I’ll be your eyes and ears. Directions we can go are “forward”, “aft (or back)”, “up”, and  “down.” It looks like we’re starting in a cool, dark place."
begin = 1

@socketio.on('input')
def myInput(event):
    print(" sending %s onwards ..." % event)
    print(request.sid)
    username_lock = False
    if username_lock:
        event['username'] = "Travis"
    if event['message']:
        if message_conts_word(event["message"], "lights"):
            socketio.emit("lights_out", True)
    if begin:
        socketio.emit("output", dict(message=beginning_str, username='bot'))
        begin = 0
    
    #GET OUT PUT
    out = getOutput()
    
    #CHAT MODS
    if message_conts_word(str(out), "Flashlight") and message_conts_word(str(out), "switch"):
        socketio.emit("lights_out", True)
    if message_conts_word(str(out), "bunks")
        event["message"] = ghostify(event["message"])
    if message_conts_word(str(out), "Engine"):
        event["message"] = only_all_caps(event["message"])
    if message_conts_word(str(out), "taste"):
        event["message"] = scramble_output(event["message"])
    
    socketio.emit("output", event) # sends to everone
    
    print(str(out))
    if not "newmedia" in str(out):
      socketio.emit("output", dict(message=str(out), username='bot'))
    time.sleep(0.5)
    if (request.sid in state):
        state[request.sid] += 1
    else:
        state[request.sid] = 0
    
    if (re.search("^{'message': 'command:", str(event))):
        time.sleep(0.5)
        comm = str(event["message"]).split(':')
        print(comm);
        print(state[request.sid], len(replies), replies)
        #print(comm[1]);
        setInput(comm[1]);
       # if not "newmedia" in str(out):
       #   socketio.emit("output", dict(message=getOutput(), username='bot'))

def check():
    while True:
        time.sleep(1)
        #socketio.emit("output", dict(message="hello from code", username="fake username"))

threading.Thread(target=check).start()

if __name__ == '__main__':
    socketio.run(app, debug=True,use_reloader=False,host='0.0.0.0' )
