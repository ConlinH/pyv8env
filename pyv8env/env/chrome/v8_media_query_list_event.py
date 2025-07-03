from .flags import *
from .v8_event import Event


@construct_111001
class MediaQueryListEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaQueryListEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("media", "get_media", None, 0, 1, 0, 0, 0, 0, 1),
        ("matches", "get_matches", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list_event.py -> MediaQueryListEvent.media -> get attr')

    def get_matches(self):
        val = self._attr.get('matches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list_event.py -> MediaQueryListEvent.matches -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list_event.py -> MediaQueryListEvent.isTrusted -> get attr')
