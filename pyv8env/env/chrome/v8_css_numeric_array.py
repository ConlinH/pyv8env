from .flags import *


@construct_1003101
class CSSNumericArray:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_css_numeric_array.py -> CSSNumericArray.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_numeric_array.py -> CSSNumericArray.length -> get attr')
