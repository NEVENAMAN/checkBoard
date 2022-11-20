from flask import Flask,render_template
app = Flask(__name__)
# -------------------------------------------------------------------
@app.route('/<row>/<column>')
def repeat(row,column):
    return render_template("index.html",row=int(row),column=int(column))

@app.route('/buildCheckBoard/<row>/<column>/<color1>/<color2>')
def buildCheckBoard(row,column,color1,color2):
    return render_template("index.html",row=int(row),column=int(column),color1=color1,color2=color2)

# -------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)