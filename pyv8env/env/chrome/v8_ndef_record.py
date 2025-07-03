from .flags import *


@construct_111001
class NDEFRecord:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("recordType", "get_recordType", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaType", "get_mediaType", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("encoding", "get_encoding", None, 0, 1, 0, 0, 0, 0, 1),
        ("lang", "get_lang", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toRecords", "fn_toRecords", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_recordType(self):
        val = self._attr.get('recordType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.recordType -> get attr')

    def get_mediaType(self):
        val = self._attr.get('mediaType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.mediaType -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.id -> get attr')

    def get_encoding(self):
        val = self._attr.get('encoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.encoding -> get attr')

    def get_lang(self):
        val = self._attr.get('lang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.lang -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.data -> get attr')

    def fn_toRecords(self, *args):
        logger.debug(f'patch -> v8_ndef_record.py -> NDEFRecord.toRecords{tuple(args)} -> method')
