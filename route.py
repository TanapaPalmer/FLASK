from flask import Flask 

app = Flask(__name__) 

@app.route('/')          
def index():
    return "Hello World!"

@app.route('/success')
def success():
    return "Success"

@app.route('/hello/<string:banana>/<int:num>')
def hello(banana,num):
    return f"Hello {banana * num}"

if __name__=="__main__":
    app.run(debug=True)

    
