from flask import Flask, render_template #追加
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, fields, validators

app = Flask(__name__)

#bootstrap使用
bootstrap = Bootstrap(app)

###########################################ページ遷移############################################
@app.route('/')
def index():
    #return name
    return render_template('index.html',titlename='ホーム')

@app.route('/blog')
def blog():
    #return name
    return render_template('blog.html',titlename='ブログ')

@app.route('/portfolio')
def portfolio():
    #return name
    return render_template('portfolio.html',titlename='ポートフォリオ')

@app.route('/about')
def about():
    #return name
    return render_template('about.html',titlename='概要')

@app.route('/contact')
def contact():
    #return name
    return render_template('contact.html',titlename='問い合わせ')

## おまじない
if __name__ == "__main__":
    app.run(debug=False)