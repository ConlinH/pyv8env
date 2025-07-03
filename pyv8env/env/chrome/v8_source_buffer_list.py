from .flags import *
from .v8_event_target import EventTarget


@construct_100101
class SourceBufferList(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SourceBufferList, self).__init__(*args, **kw)

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_source_buffer_list.py -> SourceBufferList.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("onaddsourcebuffer", "get_onaddsourcebuffer", "set_onaddsourcebuffer", 0, 1, 0, 0, 0, 0, 1),
        ("onremovesourcebuffer", "get_onremovesourcebuffer", "set_onremovesourcebuffer", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer_list.py -> SourceBufferList.length -> get attr')

    def get_onaddsourcebuffer(self):
        val = self._attr.get('onaddsourcebuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer_list.py -> SourceBufferList.onaddsourcebuffer -> get attr')

    def set_onaddsourcebuffer(self, val):
        self._attr['onaddsourcebuffer'] = val

    def get_onremovesourcebuffer(self):
        val = self._attr.get('onremovesourcebuffer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_source_buffer_list.py -> SourceBufferList.onremovesourcebuffer -> get attr')

    def set_onremovesourcebuffer(self, val):
        self._attr['onremovesourcebuffer'] = val
