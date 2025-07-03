from .flags import *


@construct_000001
class DictionaryTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("get", "fn_get", 0, 0, 1, 0, 0, 0, 0),
        ("getDerived", "fn_getDerived", 0, 0, 1, 0, 0, 0, 0),
        ("getDerivedDerived", "fn_getDerivedDerived", 0, 0, 1, 0, 0, 0, 0),
        ("set", "fn_set", 0, 0, 1, 0, 0, 0, 0),
        ("setDerived", "fn_setDerived", 1, 0, 1, 0, 0, 0, 0),
        ("setDerivedDerived", "fn_setDerivedDerived", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.get{tuple(args)} -> method')

    def fn_getDerived(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.getDerived{tuple(args)} -> method')

    def fn_getDerivedDerived(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.getDerivedDerived{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.set{tuple(args)} -> method')

    def fn_setDerived(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.setDerived{tuple(args)} -> method')

    def fn_setDerivedDerived(self, *args):
        logger.debug(f'patch -> v8_dictionary_test.py -> DictionaryTest.setDerivedDerived{tuple(args)} -> method')
