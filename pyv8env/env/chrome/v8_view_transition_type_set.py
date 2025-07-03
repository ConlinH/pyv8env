from .flags import *


@construct_100001
class ViewTransitionTypeSet:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
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

    )

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.size -> get attr')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.add{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.delete{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.entries{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.forEach{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_view_transition_type_set.py -> ViewTransitionTypeSet.values{tuple(args)} -> method')
