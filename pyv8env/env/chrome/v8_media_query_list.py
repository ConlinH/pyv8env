from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class MediaQueryList(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MediaQueryList, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("media", "get_media", None, 0, 1, 0, 0, 0, 0, 1),
        ("matches", "get_matches", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addListener", "fn_addListener", 1, 0, 1, 0, 0, 0, 0),
        ("removeListener", "fn_removeListener", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_media(self):
        val = self._attr.get('media')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list.py -> MediaQueryList.media -> get attr')

    def get_matches(self):
        val = self._attr.get('matches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list.py -> MediaQueryList.matches -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_query_list.py -> MediaQueryList.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def fn_addListener(self, *args):
        logger.debug(f'patch -> v8_media_query_list.py -> MediaQueryList.addListener{tuple(args)} -> method')

    def fn_removeListener(self, *args):
        logger.debug(f'patch -> v8_media_query_list.py -> MediaQueryList.removeListener{tuple(args)} -> method')
