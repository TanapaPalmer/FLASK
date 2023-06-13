from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key="kor_mooooooooooooooon"

@app.route('/')
def index():
    return render_template("index2.html")

@app.route('/fill_the_form',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result2')

@app.route('/result')
def success():
    return render_template('result.html2')

if __name__=="__main__":
    app.run(debug=True)