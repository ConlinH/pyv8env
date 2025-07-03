from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class PresentationConnection(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PresentationConnection, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("onconnect", "get_onconnect", "set_onconnect", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("onterminate", "get_onterminate", "set_onterminate", 0, 1, 0, 0, 0, 0, 1),
        ("binaryType", "get_binaryType", "set_binaryType", 0, 1, 0, 0, 0, 0, 1),
        ("onmessage", "get_onmessage", "set_onmessage", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("send", "fn_send", 1, 0, 1, 0, 0, 0, 0),
        ("terminate", "fn_terminate", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.id -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.url -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.state -> get attr')

    def get_onconnect(self):
        val = self._attr.get('onconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.onconnect -> get attr')

    def set_onconnect(self, val):
        self._attr['onconnect'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_onterminate(self):
        val = self._attr.get('onterminate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.onterminate -> get attr')

    def set_onterminate(self, val):
        self._attr['onterminate'] = val

    def get_binaryType(self):
        val = self._attr.get('binaryType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.binaryType -> get attr')

    def set_binaryType(self, val):
        self._attr['binaryType'] = val

    def get_onmessage(self):
        val = self._attr.get('onmessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.onmessage -> get attr')

    def set_onmessage(self, val):
        self._attr['onmessage'] = val

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.close{tuple(args)} -> method')

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.send{tuple(args)} -> method')

    def fn_terminate(self, *args):
        logger.debug(f'patch -> v8_presentation_connection.py -> PresentationConnection.terminate{tuple(args)} -> method')
