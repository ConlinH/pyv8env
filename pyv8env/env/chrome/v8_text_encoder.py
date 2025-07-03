from .flags import *


@construct_110001
class TextEncoder:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("encoding", "get_encoding", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("encode", "fn_encode", 0, 0, 1, 0, 0, 0, 0),
        ("encodeInto", "fn_encodeInto", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_encoding(self):
        val = self._attr.get('encoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_encoder.py -> TextEncoder.encoding -> get attr')

    def fn_encode(self, *args):
        logger.debug(f'patch -> v8_text_encoder.py -> TextEncoder.encode{tuple(args)} -> method')

    def fn_encodeInto(self, *args):
        logger.debug(f'patch -> v8_text_encoder.py -> TextEncoder.encodeInto{tuple(args)} -> method')
