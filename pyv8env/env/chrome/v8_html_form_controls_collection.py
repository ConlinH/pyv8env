from .flags import *
from .v8_html_collection import HTMLCollection


@construct_100101
class HTMLFormControlsCollection(HTMLCollection):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLFormControlsCollection, self).__init__(*args, **kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_set__')
            
    def __v8_name_query__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_query__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_del__')
            
    def __v8_name_enum__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_enum__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.__v8_index_desc__')
            
    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("namedItem", "fn_namedItem", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_namedItem(self, *args):
        logger.debug(f'patch -> v8_html_form_controls_collection.py -> HTMLFormControlsCollection.namedItem{tuple(args)} -> method')
