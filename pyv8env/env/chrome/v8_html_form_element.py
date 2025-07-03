from .flags import *
from .v8_html_element import HTMLElement


@construct_110101
class HTMLFormElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLFormElement, self).__init__(*args, **kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_name_set__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_name_del__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_form_element.py -> HTMLFormElement.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("acceptCharset", "get_acceptCharset", "set_acceptCharset", 0, 1, 0, 0, 0, 0, 1),
        ("action", "get_action", "set_action", 0, 1, 0, 0, 0, 0, 1),
        ("autocomplete", "get_autocomplete", "set_autocomplete", 0, 1, 0, 0, 0, 0, 1),
        ("enctype", "get_enctype", "set_enctype", 0, 1, 0, 0, 0, 0, 1),
        ("encoding", "get_encoding", "set_encoding", 0, 1, 0, 0, 0, 0, 1),
        ("method", "get_method", "set_method", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("noValidate", "get_noValidate", "set_noValidate", 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", "set_target", 0, 1, 0, 0, 0, 0, 1),
        ("rel", "get_rel", "set_rel", 0, 1, 0, 0, 0, 0, 1),
        ("relList", "get_relList", "set_relList", 0, 1, 0, 0, 0, 0, 1),
        ("elements", "get_elements", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("requestSubmit", "fn_requestSubmit", 0, 0, 1, 0, 0, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("submit", "fn_submit", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_acceptCharset(self):
        val = self._attr.get('acceptCharset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.acceptCharset -> get attr')

    def set_acceptCharset(self, val):
        self._attr['acceptCharset'] = val

    def get_action(self):
        val = self._attr.get('action')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.action -> get attr')

    def set_action(self, val):
        self._attr['action'] = val

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.autocomplete -> get attr')

    def set_autocomplete(self, val):
        self._attr['autocomplete'] = val

    def get_enctype(self):
        val = self._attr.get('enctype')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.enctype -> get attr')

    def set_enctype(self, val):
        self._attr['enctype'] = val

    def get_encoding(self):
        val = self._attr.get('encoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.encoding -> get attr')

    def set_encoding(self, val):
        self._attr['encoding'] = val

    def get_method(self):
        val = self._attr.get('method')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.method -> get attr')

    def set_method(self, val):
        self._attr['method'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_noValidate(self):
        val = self._attr.get('noValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.noValidate -> get attr')

    def set_noValidate(self, val):
        self._attr['noValidate'] = val

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.target -> get attr')

    def set_target(self, val):
        self._attr['target'] = val

    def get_rel(self):
        val = self._attr.get('rel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.rel -> get attr')

    def set_rel(self, val):
        self._attr['rel'] = val

    def get_relList(self):
        val = self._attr.get('relList')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.relList -> get attr')

    def set_relList(self, val):
        self._attr['relList'] = val

    def get_elements(self):
        val = self._attr.get('elements')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.elements -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.length -> get attr')

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.checkValidity{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.reportValidity{tuple(args)} -> method')

    def fn_requestSubmit(self, *args):
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.requestSubmit{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.reset{tuple(args)} -> method')

    def fn_submit(self, *args):
        logger.debug(f'patch -> v8_html_form_element.py -> HTMLFormElement.submit{tuple(args)} -> method')
