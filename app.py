from flask import Flask
from flask import request
from flask import render_template
#import stringComparison

from CALCULATE_COSINE import calc_cos
app = Flask(__name__)
app.config['DEBUG']=True



@app.route('/')
def my_form():

    x= render_template("my-form.html") # this should be the name of your html file
    print("get :\n",x)
    return x

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
    print("calc_cos:\n",text1)
    data = calc_cos(str(text1))
    return render_template('display.html',**data)



if __name__ == '__main__':
    app.run()