from .flags import *
from .v8_document import Document


@construct_100001
class HTMLDocument(Document):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLDocument, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("location", "get_location", "set_location", 0, 0, 4, 0, 0, 0, 1),

    )

    def get_location(self):
        val = self._attr.get('location')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_document.py -> HTMLDocument.location -> get attr')

    def set_location(self, val):
        self._attr['location'] = val
