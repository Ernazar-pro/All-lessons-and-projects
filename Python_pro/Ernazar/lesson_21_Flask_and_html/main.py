from flask import *
a=Flask(__name__)

@a.route('/')
def home():
    return render_template ('index.html')

@a.route('/about')
def about():
    return render_template('about.html')

@a.route('/<name>')
def other(name):
    with open('C:\Python_pro\Ernazar\lesson_20_Flask\data.json') as f:
        data = json.load(f)
    
    try:
            result = data[name]
    except KeyError:
            name_list = [name for name in data.keys()]
            text1='<b>Bazada tek gana tomendegi adamlardin magliwmatlari bar:</b>'
            text2='<br>'.join(name_list)
            result=f'{text1}<p>{text2}'
    return result
if __name__ =='__main__':
    a.run()
