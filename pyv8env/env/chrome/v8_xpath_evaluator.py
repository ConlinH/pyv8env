from .flags import *


@construct_110001
class XPathEvaluator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createExpression", "fn_createExpression", 1, 0, 1, 0, 0, 0, 0),
        ("createNSResolver", "fn_createNSResolver", 1, 0, 1, 0, 0, 0, 0),
        ("evaluate", "fn_evaluate", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_createExpression(self, *args):
        logger.debug(f'patch -> v8_xpath_evaluator.py -> XPathEvaluator.createExpression{tuple(args)} -> method')

    def fn_createNSResolver(self, *args):
        logger.debug(f'patch -> v8_xpath_evaluator.py -> XPathEvaluator.createNSResolver{tuple(args)} -> method')

    def fn_evaluate(self, *args):
        logger.debug(f'patch -> v8_xpath_evaluator.py -> XPathEvaluator.evaluate{tuple(args)} -> method')
