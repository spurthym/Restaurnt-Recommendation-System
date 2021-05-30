from flask import Flask
from flask import request
from flask import render_template
#import stringComparison

from CALCULATE_COSINE import calc_cos
app = Flask(__name__)
app.config['DEBUG']=True


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
    
    return(calc_cos(str(text1)))



if __name__ == '__main__':
    app.run()