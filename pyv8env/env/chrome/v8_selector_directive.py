from .flags import *
from .v8_directive import Directive


@construct_100001
class SelectorDirective(Directive):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SelectorDirective, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getMatchingRange", "fn_getMatchingRange", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_getMatchingRange(self, *args):
        logger.debug(f'patch -> v8_selector_directive.py -> SelectorDirective.getMatchingRange{tuple(args)} -> method')
