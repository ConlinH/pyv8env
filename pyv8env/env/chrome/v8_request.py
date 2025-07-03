from .flags import *


@construct_111001
class Request:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("method", "get_method", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("headers", "get_headers", None, 0, 1, 0, 0, 0, 0, 1),
        ("destination", "get_destination", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrer", "get_referrer", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),
        ("credentials", "get_credentials", None, 0, 1, 0, 0, 0, 0, 1),
        ("cache", "get_cache", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirect", "get_redirect", None, 0, 1, 0, 0, 0, 0, 1),
        ("integrity", "get_integrity", None, 0, 1, 0, 0, 0, 0, 1),
        ("keepalive", "get_keepalive", None, 0, 1, 0, 0, 0, 0, 1),
        ("signal", "get_signal", None, 0, 1, 0, 0, 0, 0, 1),
        ("isHistoryNavigation", "get_isHistoryNavigation", None, 0, 1, 0, 0, 0, 0, 1),
        ("bodyUsed", "get_bodyUsed", None, 0, 1, 0, 0, 0, 0, 1),
        ("body", "get_body", None, 0, 1, 0, 0, 0, 0, 0),
        ("targetAddressSpace", "get_targetAddressSpace", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("arrayBuffer", "fn_arrayBuffer", 0, 0, 1, 0, 1, 0, 0),
        ("blob", "fn_blob", 0, 0, 1, 0, 1, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("formData", "fn_formData", 0, 0, 1, 0, 1, 0, 0),
        ("json", "fn_json", 0, 0, 1, 0, 1, 0, 0),
        ("text", "fn_text", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_method(self):
        val = self._attr.get('method')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.method -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.url -> get attr')

    def get_headers(self):
        val = self._attr.get('headers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.headers -> get attr')

    def get_destination(self):
        val = self._attr.get('destination')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.destination -> get attr')

    def get_referrer(self):
        val = self._attr.get('referrer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.referrer -> get attr')

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.referrerPolicy -> get attr')

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.mode -> get attr')

    def get_credentials(self):
        val = self._attr.get('credentials')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.credentials -> get attr')

    def get_cache(self):
        val = self._attr.get('cache')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.cache -> get attr')

    def get_redirect(self):
        val = self._attr.get('redirect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.redirect -> get attr')

    def get_integrity(self):
        val = self._attr.get('integrity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.integrity -> get attr')

    def get_keepalive(self):
        val = self._attr.get('keepalive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.keepalive -> get attr')

    def get_signal(self):
        val = self._attr.get('signal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.signal -> get attr')

    def get_isHistoryNavigation(self):
        val = self._attr.get('isHistoryNavigation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.isHistoryNavigation -> get attr')

    def get_bodyUsed(self):
        val = self._attr.get('bodyUsed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.bodyUsed -> get attr')

    def get_body(self):
        val = self._attr.get('body')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.body -> get attr')

    def get_targetAddressSpace(self):
        val = self._attr.get('targetAddressSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_request.py -> Request.targetAddressSpace -> get attr')

    def fn_arrayBuffer(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.arrayBuffer{tuple(args)} -> method')

    def fn_blob(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.blob{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.clone{tuple(args)} -> method')

    def fn_formData(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.formData{tuple(args)} -> method')

    def fn_json(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.json{tuple(args)} -> method')

    def fn_text(self, *args):
        logger.debug(f'patch -> v8_request.py -> Request.text{tuple(args)} -> method')
