import urllib.request,json
from .models import News, NewsSource
from datetime import date

now=str(date.today())

api_key=None
base_url=None
source_url=None
def configure_request(app):
    global api_key,base_url,source_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']
    source_url=app.config['NEWS_SOURCE_API_URL']

def process_articles(news_list):
    '''
    Function that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain news details
    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_article in news_list:
        source = news_article.get('source')
        source_name = source.get('name')
        source_url= news_article.get('url')
        author_name=news_article.get('author')
        imageUrl= news_article.get('urlToImage')
        description=news_article.get('description')
        article=news_article.get('content')
        time=news_article.get('publishedAt')
        timeOfCreation=time[11:16]
        news_article = News(source_name,source_url,author_name,imageUrl,description,article,timeOfCreation)
        news_articles.append(news_article)

    return news_articles

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,now,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response= json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)
    return news_articles

# SOURCES.......................................................................
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response= json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['sources']:
            news_sources_list = get_sources_response['sources']
            news_sources = process_sources(news_sources_list)
    return news_sources

def process_sources(sources_list):
    '''
    Function that processes the news sources and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain news details
    Returns :
        news_sources: A list of sources objects
    '''
    news_sources = []
    for news_source in sources_list:
        source_id = news_source.get('id')
        source_name = news_source.get('name')
        source_url= news_source.get('url')
        source_description=news_source.get('description')
        source_category= news_source.get('category')
        source_language=news_source.get('language')

        news_source = NewsSource(source_id,source_name,source_description,source_url,source_category,source_language)
        news_sources.append(news_source)

    return news_sources