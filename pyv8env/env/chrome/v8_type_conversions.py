from .flags import *


@construct_000001
class TypeConversions:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("testLong", "get_testLong", "set_testLong", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeLong", "get_testEnforceRangeLong", "set_testEnforceRangeLong", 0, 1, 0, 0, 0, 0, 1),
        ("testUnsignedLong", "get_testUnsignedLong", "set_testUnsignedLong", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeUnsignedLong", "get_testEnforceRangeUnsignedLong", "set_testEnforceRangeUnsignedLong", 0, 1, 0, 0, 0, 0, 1),
        ("testLongLong", "get_testLongLong", "set_testLongLong", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeLongLong", "get_testEnforceRangeLongLong", "set_testEnforceRangeLongLong", 0, 1, 0, 0, 0, 0, 1),
        ("testUnsignedLongLong", "get_testUnsignedLongLong", "set_testUnsignedLongLong", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeUnsignedLongLong", "get_testEnforceRangeUnsignedLongLong", "set_testEnforceRangeUnsignedLongLong", 0, 1, 0, 0, 0, 0, 1),
        ("testByte", "get_testByte", "set_testByte", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeByte", "get_testEnforceRangeByte", "set_testEnforceRangeByte", 0, 1, 0, 0, 0, 0, 1),
        ("testOctet", "get_testOctet", "set_testOctet", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeOctet", "get_testEnforceRangeOctet", "set_testEnforceRangeOctet", 0, 1, 0, 0, 0, 0, 1),
        ("testShort", "get_testShort", "set_testShort", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeShort", "get_testEnforceRangeShort", "set_testEnforceRangeShort", 0, 1, 0, 0, 0, 0, 1),
        ("testUnsignedShort", "get_testUnsignedShort", "set_testUnsignedShort", 0, 1, 0, 0, 0, 0, 1),
        ("testEnforceRangeUnsignedShort", "get_testEnforceRangeUnsignedShort", "set_testEnforceRangeUnsignedShort", 0, 1, 0, 0, 0, 0, 1),
        ("testByteString", "get_testByteString", "set_testByteString", 0, 1, 0, 0, 0, 0, 1),
        ("testUSVString", "get_testUSVString", "set_testUSVString", 0, 1, 0, 0, 0, 0, 1),
        ("testUSVStringOrNull", "get_testUSVStringOrNull", "set_testUSVStringOrNull", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setTestByteString", "fn_setTestByteString", 1, 0, 1, 0, 0, 0, 0),
        ("setTestUSVString", "fn_setTestUSVString", 1, 0, 1, 0, 0, 0, 0),
        ("setTestUSVStringOrNull", "fn_setTestUSVStringOrNull", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_testLong(self):
        val = self._attr.get('testLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testLong -> get attr')

    def set_testLong(self, val):
        self._attr['testLong'] = val

    def get_testEnforceRangeLong(self):
        val = self._attr.get('testEnforceRangeLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeLong -> get attr')

    def set_testEnforceRangeLong(self, val):
        self._attr['testEnforceRangeLong'] = val

    def get_testUnsignedLong(self):
        val = self._attr.get('testUnsignedLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testUnsignedLong -> get attr')

    def set_testUnsignedLong(self, val):
        self._attr['testUnsignedLong'] = val

    def get_testEnforceRangeUnsignedLong(self):
        val = self._attr.get('testEnforceRangeUnsignedLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeUnsignedLong -> get attr')

    def set_testEnforceRangeUnsignedLong(self, val):
        self._attr['testEnforceRangeUnsignedLong'] = val

    def get_testLongLong(self):
        val = self._attr.get('testLongLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testLongLong -> get attr')

    def set_testLongLong(self, val):
        self._attr['testLongLong'] = val

    def get_testEnforceRangeLongLong(self):
        val = self._attr.get('testEnforceRangeLongLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeLongLong -> get attr')

    def set_testEnforceRangeLongLong(self, val):
        self._attr['testEnforceRangeLongLong'] = val

    def get_testUnsignedLongLong(self):
        val = self._attr.get('testUnsignedLongLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testUnsignedLongLong -> get attr')

    def set_testUnsignedLongLong(self, val):
        self._attr['testUnsignedLongLong'] = val

    def get_testEnforceRangeUnsignedLongLong(self):
        val = self._attr.get('testEnforceRangeUnsignedLongLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeUnsignedLongLong -> get attr')

    def set_testEnforceRangeUnsignedLongLong(self, val):
        self._attr['testEnforceRangeUnsignedLongLong'] = val

    def get_testByte(self):
        val = self._attr.get('testByte')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testByte -> get attr')

    def set_testByte(self, val):
        self._attr['testByte'] = val

    def get_testEnforceRangeByte(self):
        val = self._attr.get('testEnforceRangeByte')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeByte -> get attr')

    def set_testEnforceRangeByte(self, val):
        self._attr['testEnforceRangeByte'] = val

    def get_testOctet(self):
        val = self._attr.get('testOctet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testOctet -> get attr')

    def set_testOctet(self, val):
        self._attr['testOctet'] = val

    def get_testEnforceRangeOctet(self):
        val = self._attr.get('testEnforceRangeOctet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeOctet -> get attr')

    def set_testEnforceRangeOctet(self, val):
        self._attr['testEnforceRangeOctet'] = val

    def get_testShort(self):
        val = self._attr.get('testShort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testShort -> get attr')

    def set_testShort(self, val):
        self._attr['testShort'] = val

    def get_testEnforceRangeShort(self):
        val = self._attr.get('testEnforceRangeShort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeShort -> get attr')

    def set_testEnforceRangeShort(self, val):
        self._attr['testEnforceRangeShort'] = val

    def get_testUnsignedShort(self):
        val = self._attr.get('testUnsignedShort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testUnsignedShort -> get attr')

    def set_testUnsignedShort(self, val):
        self._attr['testUnsignedShort'] = val

    def get_testEnforceRangeUnsignedShort(self):
        val = self._attr.get('testEnforceRangeUnsignedShort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testEnforceRangeUnsignedShort -> get attr')

    def set_testEnforceRangeUnsignedShort(self, val):
        self._attr['testEnforceRangeUnsignedShort'] = val

    def get_testByteString(self):
        val = self._attr.get('testByteString')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testByteString -> get attr')

    def set_testByteString(self, val):
        self._attr['testByteString'] = val

    def get_testUSVString(self):
        val = self._attr.get('testUSVString')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testUSVString -> get attr')

    def set_testUSVString(self, val):
        self._attr['testUSVString'] = val

    def get_testUSVStringOrNull(self):
        val = self._attr.get('testUSVStringOrNull')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.testUSVStringOrNull -> get attr')

    def set_testUSVStringOrNull(self, val):
        self._attr['testUSVStringOrNull'] = val

    def fn_setTestByteString(self, *args):
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.setTestByteString{tuple(args)} -> method')

    def fn_setTestUSVString(self, *args):
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.setTestUSVString{tuple(args)} -> method')

    def fn_setTestUSVStringOrNull(self, *args):
        logger.debug(f'patch -> v8_type_conversions.py -> TypeConversions.setTestUSVStringOrNull{tuple(args)} -> method')
