from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class PresentationConnectionList(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PresentationConnectionList, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("connections", "get_connections", None, 0, 1, 0, 0, 0, 0, 1),
        ("onconnectionavailable", "get_onconnectionavailable", "set_onconnectionavailable", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_connections(self):
        val = self._attr.get('connections')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection_list.py -> PresentationConnectionList.connections -> get attr')

    def get_onconnectionavailable(self):
        val = self._attr.get('onconnectionavailable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection_list.py -> PresentationConnectionList.onconnectionavailable -> get attr')

    def set_onconnectionavailable(self, val):
        self._attr['onconnectionavailable'] = val
