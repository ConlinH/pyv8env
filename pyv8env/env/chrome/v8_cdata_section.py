from .flags import *
from .v8_text import Text


@construct_100001
class CDATASection(Text):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CDATASection, self).__init__(*args, **kw)
