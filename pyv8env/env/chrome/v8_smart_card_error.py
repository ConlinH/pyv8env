from .flags import *
from .v8_dom_exception import DOMException


@construct_112001
class SmartCardError(DOMException):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SmartCardError, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("responseCode", "get_responseCode", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_responseCode(self):
        val = self._attr.get('responseCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_smart_card_error.py -> SmartCardError.responseCode -> get attr')
