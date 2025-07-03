from .flags import *


@construct_000001
class RecordTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getNullableStringLongRecord", "fn_getNullableStringLongRecord", 0, 0, 1, 0, 0, 0, 0),
        ("getStringElementRecord", "fn_getStringElementRecord", 0, 0, 1, 0, 0, 0, 0),
        ("getStringLongRecord", "fn_getStringLongRecord", 0, 0, 1, 0, 0, 0, 0),
        ("getUSVStringUSVStringBooleanRecordRecord", "fn_getUSVStringUSVStringBooleanRecordRecord", 0, 0, 1, 0, 0, 0, 0),
        ("returnStringByteStringSequenceRecord", "fn_returnStringByteStringSequenceRecord", 0, 0, 1, 0, 0, 0, 0),
        ("setByteStringByteStringRecord", "fn_setByteStringByteStringRecord", 1, 0, 1, 0, 0, 0, 0),
        ("setFloatOrStringElementRecord", "fn_setFloatOrStringElementRecord", 1, 0, 1, 0, 0, 0, 0),
        ("setNullableStringLongRecord", "fn_setNullableStringLongRecord", 1, 0, 1, 0, 0, 0, 0),
        ("setStringElementRecord", "fn_setStringElementRecord", 1, 0, 1, 0, 0, 0, 0),
        ("setStringLongRecord", "fn_setStringLongRecord", 1, 0, 1, 0, 0, 0, 0),
        ("setUSVStringUSVStringBooleanRecordRecord", "fn_setUSVStringUSVStringBooleanRecordRecord", 1, 0, 1, 0, 0, 0, 0),
        ("unionReceivedARecord", "fn_unionReceivedARecord", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_getNullableStringLongRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.getNullableStringLongRecord{tuple(args)} -> method')

    def fn_getStringElementRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.getStringElementRecord{tuple(args)} -> method')

    def fn_getStringLongRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.getStringLongRecord{tuple(args)} -> method')

    def fn_getUSVStringUSVStringBooleanRecordRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.getUSVStringUSVStringBooleanRecordRecord{tuple(args)} -> method')

    def fn_returnStringByteStringSequenceRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.returnStringByteStringSequenceRecord{tuple(args)} -> method')

    def fn_setByteStringByteStringRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setByteStringByteStringRecord{tuple(args)} -> method')

    def fn_setFloatOrStringElementRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setFloatOrStringElementRecord{tuple(args)} -> method')

    def fn_setNullableStringLongRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setNullableStringLongRecord{tuple(args)} -> method')

    def fn_setStringElementRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setStringElementRecord{tuple(args)} -> method')

    def fn_setStringLongRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setStringLongRecord{tuple(args)} -> method')

    def fn_setUSVStringUSVStringBooleanRecordRecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.setUSVStringUSVStringBooleanRecordRecord{tuple(args)} -> method')

    def fn_unionReceivedARecord(self, *args):
        logger.debug(f'patch -> v8_record_test.py -> RecordTest.unionReceivedARecord{tuple(args)} -> method')
