from .flags import *


@construct_1003101
class DOMTokenList:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_dom_token_list.py -> DOMTokenList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 0, 0, 1, 0, 0, 0, 0),
        ("contains", "fn_contains", 1, 0, 1, 0, 0, 0, 1),
        ("item", "fn_item", 1, 0, 1, 0, 0, 0, 1),
        ("remove", "fn_remove", 0, 0, 1, 0, 0, 0, 0),
        ("replace", "fn_replace", 2, 0, 1, 0, 0, 0, 0),
        ("supports", "fn_supports", 1, 0, 1, 0, 0, 0, 0),
        ("toggle", "fn_toggle", 1, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.length -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.add{tuple(args)} -> method')

    def fn_contains(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.contains{tuple(args)} -> method')

    def fn_item(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.item{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.remove{tuple(args)} -> method')

    def fn_replace(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.replace{tuple(args)} -> method')

    def fn_supports(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.supports{tuple(args)} -> method')

    def fn_toggle(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.toggle{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_dom_token_list.py -> DOMTokenList.toString{tuple(args)} -> method')
