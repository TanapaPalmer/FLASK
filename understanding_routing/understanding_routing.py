from flask import Flask 

app = Flask(__name__) 

@app.route('/')          
def hello():
    return "Hello World!"

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<hey>')
def repeat(hey,num):
    if hey == "hey":
        return hey * num
    else:
        return  "Sorry! No response. Try again."


if __name__=="__main__":
    app.run(debug=True)

    
