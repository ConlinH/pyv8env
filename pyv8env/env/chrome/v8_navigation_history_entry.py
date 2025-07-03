from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class NavigationHistoryEntry(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NavigationHistoryEntry, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("key", "get_key", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("index", "get_index", None, 0, 1, 0, 0, 0, 0, 1),
        ("sameDocument", "get_sameDocument", None, 0, 1, 0, 0, 0, 0, 1),
        ("ondispose", "get_ondispose", "set_ondispose", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getState", "fn_getState", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_key(self):
        val = self._attr.get('key')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.key -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.id -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.url -> get attr')

    def get_index(self):
        val = self._attr.get('index')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.index -> get attr')

    def get_sameDocument(self):
        val = self._attr.get('sameDocument')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.sameDocument -> get attr')

    def get_ondispose(self):
        val = self._attr.get('ondispose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.ondispose -> get attr')

    def set_ondispose(self, val):
        self._attr['ondispose'] = val

    def fn_getState(self, *args):
        logger.debug(f'patch -> v8_navigation_history_entry.py -> NavigationHistoryEntry.getState{tuple(args)} -> method')
