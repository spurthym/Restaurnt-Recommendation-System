from flask import Flask
from flask import request
from flask import render_template
#import stringComparison

app = Flask(__name__)

text123=""
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
    global text123
    text123=text1
    return text1



if __name__ == '__main__':
    app.run()