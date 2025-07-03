from .flags import *
from .v8_style_property_map_read_only import StylePropertyMapReadOnly


@construct_100001
class StylePropertyMap(StylePropertyMapReadOnly):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(StylePropertyMap, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("append", "fn_append", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("set", "fn_set", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_append(self, *args):
        logger.debug(f'patch -> v8_style_property_map.py -> StylePropertyMap.append{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_style_property_map.py -> StylePropertyMap.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_style_property_map.py -> StylePropertyMap.delete{tuple(args)} -> method')

    def fn_set(self, *args):
        logger.debug(f'patch -> v8_style_property_map.py -> StylePropertyMap.set{tuple(args)} -> method')
