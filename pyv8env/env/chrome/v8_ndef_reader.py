from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class NDEFReader(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NDEFReader, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onreading", "get_onreading", "set_onreading", 0, 1, 0, 0, 0, 0, 1),
        ("onreadingerror", "get_onreadingerror", "set_onreadingerror", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("makeReadOnly", "fn_makeReadOnly", 0, 0, 1, 0, 1, 0, 0),
        ("scan", "fn_scan", 0, 0, 1, 0, 1, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_onreading(self):
        val = self._attr.get('onreading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_reader.py -> NDEFReader.onreading -> get attr')

    def set_onreading(self, val):
        self._attr['onreading'] = val

    def get_onreadingerror(self):
        val = self._attr.get('onreadingerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_reader.py -> NDEFReader.onreadingerror -> get attr')

    def set_onreadingerror(self, val):
        self._attr['onreadingerror'] = val

    def fn_makeReadOnly(self, *args):
        logger.debug(f'patch -> v8_ndef_reader.py -> NDEFReader.makeReadOnly{tuple(args)} -> method')

    def fn_scan(self, *args):
        logger.debug(f'patch -> v8_ndef_reader.py -> NDEFReader.scan{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_ndef_reader.py -> NDEFReader.write{tuple(args)} -> method')
