import urllib.request,json
from .models import Source
from .models import Article
apiKey=None
base_url=None

def configure_request(app):
    global apiKey,base_url,article_url
    apiKey=app.config['NEWS_API_KEY']
    base_url='https://newsapi.org/v2/sources?language=en&category={}&apiKey=d4f083d7e92c4c93a9b2cdcf591154d1'                
    article_url='https://newsapi.org/v2/top-headlines?category={}&language=en&apiKey=d4f083d7e92c4c93a9b2cdcf591154d1'

def get_source(category):
    '''
    Function that gets the json response to url request
    '''
    get_source_url= base_url.format(category,apiKey)

    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        source_results = None
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_results(source_results_list)
    return source_results



def process_results(source_list):
    source_results=[]
    for source_item in source_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')

        source_object= Source(id,name,description,url)
        source_results.append(source_object)

    return source_results



def get_articles():

    get_articles_url= article_url.format('business')

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        article_results = None
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            article_results = process_article_results(articles_results_list)
    return article_results

def process_article_results(articles_list):
    article_results=[]
    for article_item in articles_list:
        title=article_item.get('title')
        urlToImage=article_item.get('urlToImage')
        description=article_item.get('description')
        publishedAt=article_item.get('publishedAt')
        url=article_item.get('url')
        if urlToImage:
            article_object= Article(title,urlToImage,description,publishedAt,url)
            article_results.append(article_object)

    return article_results
