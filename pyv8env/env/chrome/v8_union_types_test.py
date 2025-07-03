from .flags import *


@construct_000001
class UnionTypesTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("doubleOrStringOrStringSequenceAttribute", "get_doubleOrStringOrStringSequenceAttribute", "set_doubleOrStringOrStringSequenceAttribute", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("doubleOrInternalEnumArg", "fn_doubleOrInternalEnumArg", 1, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringArg", "fn_doubleOrStringArg", 1, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringDefaultDoubleArg", "fn_doubleOrStringDefaultDoubleArg", 0, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringDefaultNullArg", "fn_doubleOrStringDefaultNullArg", 0, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringDefaultStringArg", "fn_doubleOrStringDefaultStringArg", 0, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringOrStringSequenceArg", "fn_doubleOrStringOrStringSequenceArg", 1, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringOrStringSequenceNullableArg", "fn_doubleOrStringOrStringSequenceNullableArg", 1, 0, 1, 0, 0, 0, 0),
        ("doubleOrStringSequenceArg", "fn_doubleOrStringSequenceArg", 1, 0, 1, 0, 0, 0, 0),
        ("nodeListOrElementArg", "fn_nodeListOrElementArg", 1, 0, 1, 0, 0, 0, 0),
        ("nodeListOrElementOrNullArg", "fn_nodeListOrElementOrNullArg", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_doubleOrStringOrStringSequenceAttribute(self):
        val = self._attr.get('doubleOrStringOrStringSequenceAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringOrStringSequenceAttribute -> get attr')

    def set_doubleOrStringOrStringSequenceAttribute(self, val):
        self._attr['doubleOrStringOrStringSequenceAttribute'] = val

    def fn_doubleOrInternalEnumArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrInternalEnumArg{tuple(args)} -> method')

    def fn_doubleOrStringArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringArg{tuple(args)} -> method')

    def fn_doubleOrStringDefaultDoubleArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringDefaultDoubleArg{tuple(args)} -> method')

    def fn_doubleOrStringDefaultNullArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringDefaultNullArg{tuple(args)} -> method')

    def fn_doubleOrStringDefaultStringArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringDefaultStringArg{tuple(args)} -> method')

    def fn_doubleOrStringOrStringSequenceArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringOrStringSequenceArg{tuple(args)} -> method')

    def fn_doubleOrStringOrStringSequenceNullableArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringOrStringSequenceNullableArg{tuple(args)} -> method')

    def fn_doubleOrStringSequenceArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.doubleOrStringSequenceArg{tuple(args)} -> method')

    def fn_nodeListOrElementArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.nodeListOrElementArg{tuple(args)} -> method')

    def fn_nodeListOrElementOrNullArg(self, *args):
        logger.debug(f'patch -> v8_union_types_test.py -> UnionTypesTest.nodeListOrElementOrNullArg{tuple(args)} -> method')
