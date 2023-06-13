from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", row=8, col=8, color_1='#FFEDDA', color_2='#FCB9AA')

@app.route('/<int:x>')
def checkerboard_row(x):
   return render_template("index.html", row=x, col=8, color_1='#FFEDDA', color_2='#FCB9AA')

@app.route('/<int:x>/<int:y>')
def checkerboard_row_n_col(x,y):
   return render_template("index.html", row=x, col=y, color_1='#FFEDDA', color_2='#FCB9AA')

@app.route('/<int:x>/<int:y>/<string:one>')
def checkerboard_row_n_col_x(x,y,one):
   return render_template("index.html", row=x, col=y, color_1=one, color_2='#FCB9AA')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def checkerboard_row_n_col_x_y(x,y,one,two):
   return render_template("index.html", row=x, col=y, color_1=one, color_2=two)

if __name__ == "__main__":
   app.run(debug=True)