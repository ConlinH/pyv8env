from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class SerialPort(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SerialPort, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onconnect", "get_onconnect", "set_onconnect", 0, 1, 0, 0, 0, 0, 1),
        ("ondisconnect", "get_ondisconnect", "set_ondisconnect", 0, 1, 0, 0, 0, 0, 1),
        ("readable", "get_readable", None, 0, 1, 0, 0, 0, 0, 1),
        ("writable", "get_writable", None, 0, 1, 0, 0, 0, 0, 1),
        ("connected", "get_connected", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("forget", "fn_forget", 0, 0, 1, 0, 1, 0, 0),
        ("getInfo", "fn_getInfo", 0, 0, 1, 0, 0, 0, 0),
        ("getSignals", "fn_getSignals", 0, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 1, 0, 1, 0, 1, 0, 0),
        ("setSignals", "fn_setSignals", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_onconnect(self):
        val = self._attr.get('onconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.onconnect -> get attr')

    def set_onconnect(self, val):
        self._attr['onconnect'] = val

    def get_ondisconnect(self):
        val = self._attr.get('ondisconnect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.ondisconnect -> get attr')

    def set_ondisconnect(self, val):
        self._attr['ondisconnect'] = val

    def get_readable(self):
        val = self._attr.get('readable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.readable -> get attr')

    def get_writable(self):
        val = self._attr.get('writable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.writable -> get attr')

    def get_connected(self):
        val = self._attr.get('connected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.connected -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.close{tuple(args)} -> method')

    def fn_forget(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.forget{tuple(args)} -> method')

    def fn_getInfo(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.getInfo{tuple(args)} -> method')

    def fn_getSignals(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.getSignals{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.open{tuple(args)} -> method')

    def fn_setSignals(self, *args):
        logger.debug(f'patch -> v8_serial_port.py -> SerialPort.setSignals{tuple(args)} -> method')
