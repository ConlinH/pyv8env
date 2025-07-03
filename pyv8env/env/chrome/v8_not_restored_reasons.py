from .flags import *


@construct_100001
class NotRestoredReasons:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("reasons", "get_reasons", None, 0, 1, 0, 0, 0, 0, 1),
        ("children", "get_children", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.src -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.id -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.name -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.url -> get attr')

    def get_reasons(self):
        val = self._attr.get('reasons')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.reasons -> get attr')

    def get_children(self):
        val = self._attr.get('children')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.children -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_not_restored_reasons.py -> NotRestoredReasons.toJSON{tuple(args)} -> method')
