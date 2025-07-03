from .flags import *


@construct_110001
class TextDecoder:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("encoding", "get_encoding", None, 0, 1, 0, 0, 0, 0, 1),
        ("fatal", "get_fatal", None, 0, 1, 0, 0, 0, 0, 1),
        ("ignoreBOM", "get_ignoreBOM", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("decode", "fn_decode", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_encoding(self):
        val = self._attr.get('encoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_decoder.py -> TextDecoder.encoding -> get attr')

    def get_fatal(self):
        val = self._attr.get('fatal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_decoder.py -> TextDecoder.fatal -> get attr')

    def get_ignoreBOM(self):
        val = self._attr.get('ignoreBOM')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_decoder.py -> TextDecoder.ignoreBOM -> get attr')

    def fn_decode(self, *args):
        logger.debug(f'patch -> v8_text_decoder.py -> TextDecoder.decode{tuple(args)} -> method')
