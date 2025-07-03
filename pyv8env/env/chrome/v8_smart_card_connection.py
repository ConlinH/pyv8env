from .flags import *


@construct_100001
class SmartCardConnection:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("control", "fn_control", 2, 0, 1, 0, 1, 0, 0),
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 1, 0, 0),
        ("getAttribute", "fn_getAttribute", 1, 0, 1, 0, 1, 0, 0),
        ("setAttribute", "fn_setAttribute", 2, 0, 1, 0, 1, 0, 0),
        ("startTransaction", "fn_startTransaction", 1, 0, 1, 0, 1, 0, 0),
        ("status", "fn_status", 0, 0, 1, 0, 1, 0, 0),
        ("transmit", "fn_transmit", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_control(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.control{tuple(args)} -> method')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.disconnect{tuple(args)} -> method')

    def fn_getAttribute(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.getAttribute{tuple(args)} -> method')

    def fn_setAttribute(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.setAttribute{tuple(args)} -> method')

    def fn_startTransaction(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.startTransaction{tuple(args)} -> method')

    def fn_status(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.status{tuple(args)} -> method')

    def fn_transmit(self, *args):
        logger.debug(f'patch -> v8_smart_card_connection.py -> SmartCardConnection.transmit{tuple(args)} -> method')
