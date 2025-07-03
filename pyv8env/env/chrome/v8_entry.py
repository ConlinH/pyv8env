from .flags import *


@construct_000000
class Entry:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("isFile", "get_isFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("isDirectory", "get_isDirectory", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullPath", "get_fullPath", None, 0, 1, 0, 0, 0, 0, 1),
        ("filesystem", "get_filesystem", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("copyTo", "fn_copyTo", 1, 0, 1, 0, 0, 0, 0),
        ("getMetadata", "fn_getMetadata", 1, 0, 1, 0, 0, 0, 0),
        ("getParent", "fn_getParent", 0, 0, 1, 0, 0, 0, 0),
        ("moveTo", "fn_moveTo", 1, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 1, 0, 1, 0, 0, 0, 0),
        ("toURL", "fn_toURL", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_isFile(self):
        val = self._attr.get('isFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_entry.py -> Entry.isFile -> get attr')

    def get_isDirectory(self):
        val = self._attr.get('isDirectory')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_entry.py -> Entry.isDirectory -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_entry.py -> Entry.name -> get attr')

    def get_fullPath(self):
        val = self._attr.get('fullPath')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_entry.py -> Entry.fullPath -> get attr')

    def get_filesystem(self):
        val = self._attr.get('filesystem')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_entry.py -> Entry.filesystem -> get attr')

    def fn_copyTo(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.copyTo{tuple(args)} -> method')

    def fn_getMetadata(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.getMetadata{tuple(args)} -> method')

    def fn_getParent(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.getParent{tuple(args)} -> method')

    def fn_moveTo(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.moveTo{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.remove{tuple(args)} -> method')

    def fn_toURL(self, *args):
        logger.debug(f'patch -> v8_entry.py -> Entry.toURL{tuple(args)} -> method')
