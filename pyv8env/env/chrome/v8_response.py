from .flags import *


@construct_110001
class Response:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("redirected", "get_redirected", None, 0, 1, 0, 0, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),
        ("ok", "get_ok", None, 0, 1, 0, 0, 0, 0, 1),
        ("statusText", "get_statusText", None, 0, 1, 0, 0, 0, 0, 1),
        ("headers", "get_headers", None, 0, 1, 0, 0, 0, 0, 1),
        ("body", "get_body", None, 0, 1, 0, 0, 0, 0, 0),
        ("bodyUsed", "get_bodyUsed", None, 0, 1, 0, 0, 0, 0, 1),

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
        ("error", "fn_error", 0, 0, 2, 0, 1, 1, 0),
        ("redirect", "fn_redirect", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.type -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.url -> get attr')

    def get_redirected(self):
        val = self._attr.get('redirected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.redirected -> get attr')

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.status -> get attr')

    def get_ok(self):
        val = self._attr.get('ok')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.ok -> get attr')

    def get_statusText(self):
        val = self._attr.get('statusText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.statusText -> get attr')

    def get_headers(self):
        val = self._attr.get('headers')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.headers -> get attr')

    def get_body(self):
        val = self._attr.get('body')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.body -> get attr')

    def get_bodyUsed(self):
        val = self._attr.get('bodyUsed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_response.py -> Response.bodyUsed -> get attr')

    def fn_arrayBuffer(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.arrayBuffer{tuple(args)} -> method')

    def fn_blob(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.blob{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.clone{tuple(args)} -> method')

    def fn_formData(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.formData{tuple(args)} -> method')

    def fn_json(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.json{tuple(args)} -> method')

    def fn_text(self, *args):
        logger.debug(f'patch -> v8_response.py -> Response.text{tuple(args)} -> method')

    @classmethod
    def fn_error(cls, *args):
        logger.debug(f'patch -> v8_response.py -> Response.error{tuple(args)} -> method')

    @classmethod
    def fn_redirect(cls, *args):
        logger.debug(f'patch -> v8_response.py -> Response.redirect{tuple(args)} -> method')
