from flask import Flask,render_template,url_for,request,session,redirect
from settings import Settings
import json
from pymongo import MongoClient
from flask_pymongo import PyMongo
#check_userid = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.check_user]




app = Flask(__name__)
app.config["MONGO_DBNAME"]="usr"
app.config["MONGO_URL"]="MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.check_user]"

mongo=PyMongo(app)

@app.route('/',methods=["POST"])
def index():
    return render_template('api.html')

if (__name__ == '__main__'):
	app.secret_key="secrev tivekey"
	app.run(debug=True)
 	