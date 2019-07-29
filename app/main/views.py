from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news,get_sources
# , get_a_news, search_news

@main.route('/')

def index():

    '''
    This view function returns the index page and its data
    '''

    news_sources=get_sources()
    title = 'Home - Welcome to the best NEWS UPDATES site online'
    search_news = request.args.get('news_query')
    if search_news:
         return redirect(url_for('main.search',news_name= search_news))
    else:

        return render_template('index.html',title=title, sources=news_sources)

@main.route('/highlights')

def highlights():
    '''
    View news highlights function return highlights of news
    '''
    todays_highlights = get_news("general")
    todays_weather = get_news('weather')
    todays_sports = get_news('sports')

    return render_template('highlights.html', general=todays_highlights ,weather=todays_weather,sports=todays_sports)

@main.route('/search/<news_name>')

def search(news_name):
    '''
    View function to display the search results
    '''
    searched_news = get_news(news_name)
    title = f'search results for {news_name}'

    return render_template('search.html',news = searched_news)
