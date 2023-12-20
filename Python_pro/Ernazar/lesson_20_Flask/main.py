from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "it's <b>true</b>"

@app.route('/about')
def about():
    return "Bul sayt Keleshek Akademiyasi oqiwshilari ushin jaratilg'an"

@app.route('/<Facebook>')
def other(facebook):
    return facebook

if __name__ == '__main__':
    app.run()