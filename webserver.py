from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Sono Vivo, code in https://replit.com/@ValmouseProgram/Bot-DVGSERVER-DS#main.py"



def run():
  app.run(host='0.0.0.0',port=8080)



def keep_alive():  
    t = Thread(target=run)
    t.start()