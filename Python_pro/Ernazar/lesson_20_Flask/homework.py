import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "it's <b>true</b>"

@app.route('/about')
def about():
    return "Bul sayt Keleshek Akademiyasi oqiwshilari ushin jaratilg'an"

@app.route('/<name>')
def about_name(name):
    with open('C:\Python_pro\Ernazar\lesson_20\data.json','r') as file:
        data = json.load(file)
    return data[name] 

if __name__ == '__main__':
    app.run()
