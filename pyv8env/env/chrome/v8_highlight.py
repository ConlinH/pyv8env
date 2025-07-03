from .flags import *


@construct_110001
class Highlight:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("priority", "get_priority", "set_priority", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("forEach", "fn_forEach", 1, 0, 1, 0, 0, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),
        ("addEventListener", "fn_addEventListener", 2, 0, 1, 0, 0, 0, 0),
        ("dispatchEvent", "fn_dispatchEvent", 1, 0, 1, 0, 0, 0, 0),
        ("removeEventListener", "fn_removeEventListener", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_priority(self):
        val = self._attr.get('priority')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_highlight.py -> Highlight.priority -> get attr')

    def set_priority(self, val):
        self._attr['priority'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_highlight.py -> Highlight.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_highlight.py -> Highlight.size -> get attr')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.add{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.delete{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.entries{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.forEach{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.values{tuple(args)} -> method')

    def fn_addEventListener(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.addEventListener{tuple(args)} -> method')

    def fn_dispatchEvent(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.dispatchEvent{tuple(args)} -> method')

    def fn_removeEventListener(self, *args):
        logger.debug(f'patch -> v8_highlight.py -> Highlight.removeEventListener{tuple(args)} -> method')
