from .flags import *


@construct_100101
class SVGNumberList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_svg_number_list.py -> SVGNumberList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberOfItems", "get_numberOfItems", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("appendItem", "fn_appendItem", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("getItem", "fn_getItem", 1, 0, 1, 0, 0, 0, 0),
        ("initialize", "fn_initialize", 1, 0, 1, 0, 0, 0, 0),
        ("insertItemBefore", "fn_insertItemBefore", 2, 0, 1, 0, 0, 0, 0),
        ("removeItem", "fn_removeItem", 1, 0, 1, 0, 0, 0, 0),
        ("replaceItem", "fn_replaceItem", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.length -> get attr')

    def get_numberOfItems(self):
        val = self._attr.get('numberOfItems')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.numberOfItems -> get attr')

    def fn_appendItem(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.appendItem{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.clear{tuple(args)} -> method')

    def fn_getItem(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.getItem{tuple(args)} -> method')

    def fn_initialize(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.initialize{tuple(args)} -> method')

    def fn_insertItemBefore(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.insertItemBefore{tuple(args)} -> method')

    def fn_removeItem(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.removeItem{tuple(args)} -> method')

    def fn_replaceItem(self, *args):
        logger.debug(f'patch -> v8_svg_number_list.py -> SVGNumberList.replaceItem{tuple(args)} -> method')
