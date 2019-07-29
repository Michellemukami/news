class News:
    '''
    News class to define News Objects
    '''

    def __init__(self, source_name, source_url, author_name, imageUrl, description, article, timeOfCreation):
        self.source_name=source_name
        self.source_url=source_url
        self.author_name=author_name
        self.imageUrl=imageUrl
        self.description=description
        self.article=article
        self.timeOfCreation=timeOfCreation

class NewsSource:
    '''
    NewsSource class to define sources Objects
    '''
    def __init__(self,source_id,source_name,source_description,source_url,source_category,source_language):
        self.source_id=source_id
        self.source_name=source_name
        self.source_description=source_description
        self.source_url=source_url
        self.source_category=source_category
        self.source_language=source_language
