import requests

class Movies(object):
    """docstring for Movies."""
    def __init__(self,
                 title,
                 synopsis,
                 gender,
                 situation,
                 duration,
                 keyword,
                 homepage,
                 year,
                 cover):
        super(Movies, self).__init__()
        self.title = title
        self.synopsis = synopsis
        self.gender = gender
        self.situation = situation
        self.duration = duration
        self.keyword = keyword
        self.homepage = homepage
        self.year = year
        self.cover = cover
