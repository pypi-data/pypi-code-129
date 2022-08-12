from bs4 import BeautifulSoup
import requests
class YTagFinder:
    """
        YTageFinder is a module to fetch a 
    """
    result = []
    def __init__(self):
        pass

    def find_tags(self, youtube_video_url:str, return_type='list') -> list:
        
        if 'list' == return_type or return_type == 'string':
            page = requests.get(youtube_video_url)
            b = BeautifulSoup(page.content, features='html.parser')
            f = b.findAll("meta", {"name":"keywords"})
            tags = f[0]['content']
            if return_type == 'list':
                list_tags = tags.split(', ')
                return list_tags
            return tags
        else:
            raise YTagFinderError("return type not recognize. All avalaible return type: list (default), string")
class YTagFinderError(Exception):
    pass

y = YTagFinder()
print(y.find_tags('https://www.youtube.com/watch?v=QPdk3heGD10', return_type='string'))