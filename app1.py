from flask import Flask
from flask import request
from flask import render_template


import json
from pymongo import MongoClient
from settings import Settings
#import stringComparison

from CALCULATE_COSINE import calc_cos
app = Flask(__name__)
app.config['DEBUG']=True
rec = MongoClient(Settings.MONGO_CONNECTION_STRING)[Settings.USER_DATABASE][Settings.rmdr] #collection name is test

rec_cursor = rec.find()
l=[]


@app.route('/')
def my_form():
    return render_template("my-form.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    text1 = request.form['text1']
    '''
    plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
    if plagiarismPercent > 50 :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>No Plagiarism Detected !</h1>"

    '''
    s=""
    for x in rec_cursor:
    	if text1==x["Business id"]:
    		l.append(x["Business id"])
    		l.append(x["Stars"])
    		l.append(x["Service"])
    		l.append(x["Cleanliness"])
    		l.append(x["Authenticity"])
    		l.append(x["Value for money"])

    		s=' '.join(l)

    return (s)



if __name__ == '__main__':
    app.run()