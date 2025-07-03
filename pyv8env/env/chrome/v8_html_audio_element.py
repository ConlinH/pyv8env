from .flags import *
from .v8_html_media_element import HTMLMediaElement


@construct_110001
class HTMLAudioElement(HTMLMediaElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLAudioElement, self).__init__(*args, **kw)
