from flask import Flask, render_template
from webapp.model import db, News
from webapp.weather import weather_by_city
from webapp.forms import LoginForm


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():    
        title = 'Новости Python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])    
        news_list = News.query.order_by(News.published.desc()).all()
        #print(news_list)
        return render_template('index2.html', page_title = title, weather = weather, news_list = 'news_list')
        

    @app.route('/')
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template ('login.html',page_title = title, form = login_form)
    
    return app
#set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

