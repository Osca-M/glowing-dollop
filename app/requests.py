from newsapi import NewsApiClient

from .models import Sources, Articles, Headlines

key = None
newsapi = None


def configure_request(app):
    global key, newsapi
    key = app.config['NEWS_API_KEY']
    newsapi = NewsApiClient(api_key=key)


def sources():
    """
    function that gets all english news sources in a list
    """
    data = newsapi.get_sources(language='en', country='ca')
    data_list = data['sources']
    source_list = []
    for item in data_list:
        new_source = Sources(item['id'], item['name'], item['description'], item['url'])
        source_list.append(new_source)

    return source_list


def headlines():
    """
    function that gets all english nes sources in a list
    """
    res = newsapi.get_top_headlines(language='en', page_size=6, sources='cnn')
    res_list = res['articles']
    trending = []
    for item in res_list:
        top_article = Headlines(item['title'], item['urlToImage'], item['url'])
        trending.append(top_article)

    return trending


def articles(source_id):
    """
    function that gets all english news sources in a list
    """
    # url = everything_url.format(source_id, key)
    # with urllib.request.urlopen(url) as uri:
    #     result = uri.read()
    #     response = json.loads(result)
    article_results = []
    response = newsapi.get_everything(sources=source_id)
    if response['articles']:
        article_results = get_data(response['articles'])
    return article_results


def get_data(source_dict):
    """
    """
    article_list = []
    for item in source_dict:
        title = item.get('title')
        author = item.get('author')
        description = item.get('description')
        url = item.get('url')
        url_to_image = item.get('urlToImage')
        published_at = item.get('publishedAt')

        if url_to_image and url:
            new_article = Articles(title, author, description, url, url_to_image, published_at)
            article_list.append(new_article)
    return article_list
