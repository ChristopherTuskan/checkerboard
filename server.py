from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard():
    return render_template('index.html',row=8, column=8,color1='red',color2='black')

@app.route('/<int:y>')
def modRow(y):
    return render_template('index.html',row=y, column=8,color1='red',color2='black')

@app.route('/<int:y>/<int:x>')
def modRowAndColumns(y,x):
    return render_template('index.html',row=y, column=x,color1='red',color2='black')

@app.route('/<int:y>/<int:x>/<string:colorFirst>/<string:colorSecond>')
def modAll(y,x,colorFirst,colorSecond):
    return render_template('index.html',row=y, column=x,color1=colorFirst,color2=colorSecond)














if __name__=='__main__':
    app.run(debug=True)