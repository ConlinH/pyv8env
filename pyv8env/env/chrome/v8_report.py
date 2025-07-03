from .flags import *


@construct_000000
class Report:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("body", "get_body", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_report.py -> Report.type -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_report.py -> Report.url -> get attr')

    def get_body(self):
        val = self._attr.get('body')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_report.py -> Report.body -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_report.py -> Report.toJSON{tuple(args)} -> method')
