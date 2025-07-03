from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class FileReader(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileReader, self).__init__(*args, **kw)
    EMPTY = 0
    LOADING = 1
    DONE = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("onloadstart", "get_onloadstart", "set_onloadstart", 0, 1, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 1, 0, 0, 0, 0, 1),
        ("onload", "get_onload", "set_onload", 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onloadend", "get_onloadend", "set_onloadend", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("readAsArrayBuffer", "fn_readAsArrayBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("readAsBinaryString", "fn_readAsBinaryString", 1, 0, 1, 0, 0, 0, 0),
        ("readAsDataURL", "fn_readAsDataURL", 1, 0, 1, 0, 0, 0, 0),
        ("readAsText", "fn_readAsText", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.readyState -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.result -> get attr')

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.error -> get attr')

    def get_onloadstart(self):
        val = self._attr.get('onloadstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onloadstart -> get attr')

    def set_onloadstart(self, val):
        self._attr['onloadstart'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onload(self):
        val = self._attr.get('onload')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onload -> get attr')

    def set_onload(self, val):
        self._attr['onload'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onloadend(self):
        val = self._attr.get('onloadend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.onloadend -> get attr')

    def set_onloadend(self, val):
        self._attr['onloadend'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.abort{tuple(args)} -> method')

    def fn_readAsArrayBuffer(self, *args):
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.readAsArrayBuffer{tuple(args)} -> method')

    def fn_readAsBinaryString(self, *args):
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.readAsBinaryString{tuple(args)} -> method')

    def fn_readAsDataURL(self, *args):
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.readAsDataURL{tuple(args)} -> method')

    def fn_readAsText(self, *args):
        logger.debug(f'patch -> v8_file_reader.py -> FileReader.readAsText{tuple(args)} -> method')
