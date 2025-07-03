from .flags import *
from .v8_character_data import CharacterData


@construct_110001
class Comment(CharacterData):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Comment, self).__init__(*args, **kw)
