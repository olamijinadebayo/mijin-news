class Source:
    '''
    this class will be used to instantiate source objects
    '''
    def __init__(self,id,name,description):
        self.id = id
        self.name = name
        self.description = description

class Article(object):
    """this class will be used to instantiate article objects"""
    def __init__(self,source,title,urlToImage,description,urlToArticle,publishedAt):
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.urlToArticle = urlToArticle
        self.publishedAt = publishedAt
