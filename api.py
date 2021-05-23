from flask import Flask,render


app = Flask(__name__)
app.config['DEBUG']=True

if __name__== '__main__':
	api.run()

@app.route("/")
def index():
    return "Congratulations, it's a web app!"