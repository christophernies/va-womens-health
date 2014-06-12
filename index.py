from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index3.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
