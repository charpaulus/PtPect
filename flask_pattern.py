import json

from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Home page'
    param['username'] = 'User'
    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf-8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
