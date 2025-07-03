from .flags import *


@construct_100001
class PressureRecord:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("source", "get_source", None, 0, 1, 0, 0, 0, 0, 1),
        ("state", "get_state", None, 0, 1, 0, 0, 0, 0, 1),
        ("time", "get_time", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_source(self):
        val = self._attr.get('source')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pressure_record.py -> PressureRecord.source -> get attr')

    def get_state(self):
        val = self._attr.get('state')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pressure_record.py -> PressureRecord.state -> get attr')

    def get_time(self):
        val = self._attr.get('time')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pressure_record.py -> PressureRecord.time -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_pressure_record.py -> PressureRecord.toJSON{tuple(args)} -> method')
