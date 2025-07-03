from .flags import *
from .v8_dom_exception import DOMException


@construct_111001
class OverconstrainedError(DOMException):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OverconstrainedError, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("constraint", "get_constraint", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_constraint(self):
        val = self._attr.get('constraint')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_overconstrained_error.py -> OverconstrainedError.constraint -> get attr')
