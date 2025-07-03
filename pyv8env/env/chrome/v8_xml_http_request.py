from .flags import *
from .v8_xml_http_request_event_target import XMLHttpRequestEventTarget


@construct_110001
class XMLHttpRequest(XMLHttpRequestEventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XMLHttpRequest, self).__init__(*args, **kw)
    UNSENT = 0
    OPENED = 1
    HEADERS_RECEIVED = 2
    LOADING = 3
    DONE = 4

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onreadystatechange", "get_onreadystatechange", "set_onreadystatechange", 0, 1, 0, 0, 0, 0, 1),
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("timeout", "get_timeout", "set_timeout", 0, 1, 0, 0, 0, 0, 1),
        ("withCredentials", "get_withCredentials", "set_withCredentials", 0, 1, 0, 0, 0, 0, 1),
        ("upload", "get_upload", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseURL", "get_responseURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),
        ("statusText", "get_statusText", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseType", "get_responseType", "set_responseType", 0, 1, 0, 0, 0, 0, 1),
        ("response", "get_response", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseText", "get_responseText", None, 0, 1, 0, 0, 0, 0, 1),
        ("responseXML", "get_responseXML", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("getAllResponseHeaders", "fn_getAllResponseHeaders", 0, 0, 1, 0, 0, 0, 0),
        ("getResponseHeader", "fn_getResponseHeader", 1, 0, 1, 0, 0, 0, 0),
        ("open", "fn_open", 2, 0, 1, 0, 0, 0, 0),
        ("overrideMimeType", "fn_overrideMimeType", 1, 0, 1, 0, 0, 0, 0),
        ("send", "fn_send", 0, 0, 1, 0, 0, 0, 0),
        ("setRequestHeader", "fn_setRequestHeader", 2, 0, 1, 0, 0, 0, 0),
        ("setAttributionReporting", "fn_setAttributionReporting", 1, 0, 1, 0, 0, 0, 0),
        ("setPrivateToken", "fn_setPrivateToken", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_onreadystatechange(self):
        val = self._attr.get('onreadystatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.onreadystatechange -> get attr')

    def set_onreadystatechange(self, val):
        self._attr['onreadystatechange'] = val

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.readyState -> get attr')

    def get_timeout(self):
        val = self._attr.get('timeout')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.timeout -> get attr')

    def set_timeout(self, val):
        self._attr['timeout'] = val

    def get_withCredentials(self):
        val = self._attr.get('withCredentials')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.withCredentials -> get attr')

    def set_withCredentials(self, val):
        self._attr['withCredentials'] = val

    def get_upload(self):
        val = self._attr.get('upload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.upload -> get attr')

    def get_responseURL(self):
        val = self._attr.get('responseURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.responseURL -> get attr')

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.status -> get attr')

    def get_statusText(self):
        val = self._attr.get('statusText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.statusText -> get attr')

    def get_responseType(self):
        val = self._attr.get('responseType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.responseType -> get attr')

    def set_responseType(self, val):
        self._attr['responseType'] = val

    def get_response(self):
        val = self._attr.get('response')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.response -> get attr')

    def get_responseText(self):
        val = self._attr.get('responseText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.responseText -> get attr')

    def get_responseXML(self):
        val = self._attr.get('responseXML')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.responseXML -> get attr')

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.abort{tuple(args)} -> method')

    def fn_getAllResponseHeaders(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.getAllResponseHeaders{tuple(args)} -> method')

    def fn_getResponseHeader(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.getResponseHeader{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.open{tuple(args)} -> method')

    def fn_overrideMimeType(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.overrideMimeType{tuple(args)} -> method')

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.send{tuple(args)} -> method')

    def fn_setRequestHeader(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.setRequestHeader{tuple(args)} -> method')

    def fn_setAttributionReporting(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.setAttributionReporting{tuple(args)} -> method')

    def fn_setPrivateToken(self, *args):
        logger.debug(f'patch -> v8_xml_http_request.py -> XMLHttpRequest.setPrivateToken{tuple(args)} -> method')
