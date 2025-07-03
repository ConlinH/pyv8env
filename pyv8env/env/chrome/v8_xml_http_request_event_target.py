from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class XMLHttpRequestEventTarget(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XMLHttpRequestEventTarget, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onloadstart", "get_onloadstart", "set_onloadstart", 0, 1, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onload", "get_onload", "set_onload", 0, 1, 0, 0, 0, 0, 1),
        ("ontimeout", "get_ontimeout", "set_ontimeout", 0, 1, 0, 0, 0, 0, 1),
        ("onloadend", "get_onloadend", "set_onloadend", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_onloadstart(self):
        val = self._attr.get('onloadstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onloadstart -> get attr')

    def set_onloadstart(self, val):
        self._attr['onloadstart'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_ontimeout(self):
        val = self._attr.get('ontimeout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.ontimeout -> get attr')

    def set_ontimeout(self, val):
        self._attr['ontimeout'] = val

    def get_onloadend(self):
        val = self._attr.get('onloadend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request_event_target.py -> XMLHttpRequestEventTarget.onloadend -> get attr')

    def set_onloadend(self, val):
        self._attr['onloadend'] = val
