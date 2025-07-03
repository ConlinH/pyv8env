from .flags import *


@construct_100001
class GPUBuffer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),
        ("usage", "get_usage", None, 0, 1, 0, 0, 0, 0, 1),
        ("mapState", "get_mapState", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),
        ("getMappedRange", "fn_getMappedRange", 0, 0, 1, 0, 0, 0, 0),
        ("mapAsync", "fn_mapAsync", 1, 0, 1, 0, 1, 0, 0),
        ("unmap", "fn_unmap", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.size -> get attr')

    def get_usage(self):
        val = self._attr.get('usage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.usage -> get attr')

    def get_mapState(self):
        val = self._attr.get('mapState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.mapState -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.destroy{tuple(args)} -> method')

    def fn_getMappedRange(self, *args):
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.getMappedRange{tuple(args)} -> method')

    def fn_mapAsync(self, *args):
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.mapAsync{tuple(args)} -> method')

    def fn_unmap(self, *args):
        logger.debug(f'patch -> v8_gpu_buffer.py -> GPUBuffer.unmap{tuple(args)} -> method')
