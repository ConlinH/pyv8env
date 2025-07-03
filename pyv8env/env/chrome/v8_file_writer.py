from .flags import *
from .v8_event_target import EventTarget


@construct_000000
class FileWriter(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FileWriter, self).__init__(*args, **kw)
    INIT = 0
    WRITING = 1
    DONE = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("readyState", "get_readyState", None, 0, 1, 0, 0, 0, 0, 1),
        ("error", "get_error", None, 0, 1, 0, 0, 0, 0, 1),
        ("position", "get_position", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("onwritestart", "get_onwritestart", "set_onwritestart", 0, 1, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 1, 0, 0, 0, 0, 1),
        ("onwrite", "get_onwrite", "set_onwrite", 0, 1, 0, 0, 0, 0, 1),
        ("onabort", "get_onabort", "set_onabort", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onwriteend", "get_onwriteend", "set_onwriteend", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 0, 0, 0),
        ("seek", "fn_seek", 1, 0, 1, 0, 0, 0, 0),
        ("truncate", "fn_truncate", 1, 0, 1, 0, 0, 0, 0),
        ("write", "fn_write", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_readyState(self):
        val = self._attr.get('readyState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.readyState -> get attr')

    def get_error(self):
        val = self._attr.get('error')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.error -> get attr')

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.position -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.length -> get attr')

    def get_onwritestart(self):
        val = self._attr.get('onwritestart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onwritestart -> get attr')

    def set_onwritestart(self, val):
        self._attr['onwritestart'] = val

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def get_onwrite(self):
        val = self._attr.get('onwrite')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onwrite -> get attr')

    def set_onwrite(self, val):
        self._attr['onwrite'] = val

    def get_onabort(self):
        val = self._attr.get('onabort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onabort -> get attr')

    def set_onabort(self, val):
        self._attr['onabort'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onwriteend(self):
        val = self._attr.get('onwriteend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.onwriteend -> get attr')

    def set_onwriteend(self, val):
        self._attr['onwriteend'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.abort{tuple(args)} -> method')

    def fn_seek(self, *args):
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.seek{tuple(args)} -> method')

    def fn_truncate(self, *args):
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.truncate{tuple(args)} -> method')

    def fn_write(self, *args):
        logger.debug(f'patch -> v8_file_writer.py -> FileWriter.write{tuple(args)} -> method')
