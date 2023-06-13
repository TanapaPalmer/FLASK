from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play_basic():
    return render_template("index.html",num=3, color="lightblue")

@app.route('/play/<int:num>')
def play_intermediate(num):
    return render_template("index.html", num=num, color="lightblue")

@app.route('/play/<int:num>/<string:color>')
def play_advanced(num,color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)
