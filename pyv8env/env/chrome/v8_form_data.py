from .flags import *


@construct_110001
class FormData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("append", "fn_append", 2, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 0, 0, 0),
        ("getAll", "fn_getAll", 1, 0, 1, 0, 0, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 0, 0, 0),
        ("set", "fn_set", 2, 0, 1, 0, 0, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("forEach", "fn_forEach", 1, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.append{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.delete{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.get{tuple(args)} -> method')

    def fn_getAll(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.getAll{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.has{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.set{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.entries{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.forEach{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_form_data.py -> FormData.values{tuple(args)} -> method')
