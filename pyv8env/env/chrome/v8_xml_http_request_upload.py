from .flags import *
from .v8_xml_http_request_event_target import XMLHttpRequestEventTarget


@construct_100001
class XMLHttpRequestUpload(XMLHttpRequestEventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XMLHttpRequestUpload, self).__init__(*args, **kw)
