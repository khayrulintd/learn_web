from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.python_org_news import get_python_news


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():    
        title = 'Новости Python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])    
        news_list = get_python_news()
        #print(news_list)
        return render_template('index1.html', page_title = title, weather = weather, news_list = 'news_list')

    return app

#C:\\projects\\learnweb2\\webapp\\templates\\index1.html
