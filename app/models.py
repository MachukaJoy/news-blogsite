class Article:
    '''
    Article class to define article Objects
    '''

    def __init__(self,title,urlToImage,description,publishedAt,url):
        self.title=title
        self.urlToImage=urlToImage
        self.description=description
        self.publishedAt=publishedAt
        self.url=url


class Source:
    '''
    Source  class to define source Objects
    '''

    def __init__(self,id,name,description,url):
        self.id=id
        self.name=name
        self.description=description
        self.url=url 