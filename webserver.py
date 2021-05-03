from flask import Flask, render_template
from threading import Thread 

app = Flask('')



@app.route('/')
def source():
    return "Webserver OK, Discord Bot OK"

def run():
  app.run(host='0.0.0.0',port=8080)



def keep_alive():  
    t = Thread(target=run)
    t.start()