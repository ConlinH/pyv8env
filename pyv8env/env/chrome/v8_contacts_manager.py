from .flags import *


@construct_100001
class ContactsManager:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getProperties", "fn_getProperties", 0, 0, 1, 0, 1, 0, 0),
        ("select", "fn_select", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_getProperties(self, *args):
        logger.debug(f'patch -> v8_contacts_manager.py -> ContactsManager.getProperties{tuple(args)} -> method')

    def fn_select(self, *args):
        logger.debug(f'patch -> v8_contacts_manager.py -> ContactsManager.select{tuple(args)} -> method')
