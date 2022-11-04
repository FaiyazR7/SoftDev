'''
Green Monkeys; Daniel He, Faiyaz Rafee
SoftDev
K19 -- Cookies
2022-11-3
time spent:
'''
from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session

app = Flask(__name__)    #create Flask object
app.secret_key = b"hehe"
@app.route("/daniel")

def sessionCreate():
    if request.method == 'GET':
        session["username"] = request.args["username"]
    print (request.args["username"])
    return render_template("response.html")


@app.route("/")
def welcome():

    if "username" in session: 
        return "Welcome" + session["username"]

    else:
        return render_template("login.html")
            
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
