from .flags import *


@construct_100001
class XPathExpression:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("evaluate", "fn_evaluate", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_evaluate(self, *args):
        logger.debug(f'patch -> v8_xpath_expression.py -> XPathExpression.evaluate{tuple(args)} -> method')
