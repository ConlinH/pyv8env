from .flags import *


@construct_000001
class CallbackFunctionTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("testCallback", "fn_testCallback", 3, 0, 1, 0, 0, 0, 0),
        ("testEnumCallback", "fn_testEnumCallback", 2, 0, 1, 0, 0, 0, 0),
        ("testInterfaceCallback", "fn_testInterfaceCallback", 2, 0, 1, 0, 0, 0, 0),
        ("testNullableCallback", "fn_testNullableCallback", 3, 0, 1, 0, 0, 0, 0),
        ("testReceiverObjectCallback", "fn_testReceiverObjectCallback", 1, 0, 1, 0, 0, 0, 0),
        ("testSequenceCallback", "fn_testSequenceCallback", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_testCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testCallback{tuple(args)} -> method')

    def fn_testEnumCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testEnumCallback{tuple(args)} -> method')

    def fn_testInterfaceCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testInterfaceCallback{tuple(args)} -> method')

    def fn_testNullableCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testNullableCallback{tuple(args)} -> method')

    def fn_testReceiverObjectCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testReceiverObjectCallback{tuple(args)} -> method')

    def fn_testSequenceCallback(self, *args):
        logger.debug(f'patch -> v8_callback_function_test.py -> CallbackFunctionTest.testSequenceCallback{tuple(args)} -> method')
