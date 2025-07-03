from .flags import *
from .v8_event import Event


@construct_112001
class NavigationCurrentEntryChangeEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NavigationCurrentEntryChangeEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("navigationType", "get_navigationType", None, 0, 1, 0, 0, 0, 0, 1),
        ("from", "get_from", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_navigationType(self):
        val = self._attr.get('navigationType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_current_entry_change_event.py -> NavigationCurrentEntryChangeEvent.navigationType -> get attr')

    def get_from(self):
        val = self._attr.get('from')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_current_entry_change_event.py -> NavigationCurrentEntryChangeEvent.from -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation_current_entry_change_event.py -> NavigationCurrentEntryChangeEvent.isTrusted -> get attr')
