from .flags import *


@construct_100001
class GPUQueue:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("copyExternalImageToTexture", "fn_copyExternalImageToTexture", 3, 0, 1, 0, 0, 0, 0),
        ("onSubmittedWorkDone", "fn_onSubmittedWorkDone", 0, 0, 1, 0, 1, 0, 0),
        ("submit", "fn_submit", 1, 0, 1, 0, 0, 0, 0),
        ("writeBuffer", "fn_writeBuffer", 3, 0, 1, 0, 0, 0, 0),
        ("writeTexture", "fn_writeTexture", 4, 0, 1, 0, 0, 0, 0),

    )

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_copyExternalImageToTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.copyExternalImageToTexture{tuple(args)} -> method')

    def fn_onSubmittedWorkDone(self, *args):
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.onSubmittedWorkDone{tuple(args)} -> method')

    def fn_submit(self, *args):
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.submit{tuple(args)} -> method')

    def fn_writeBuffer(self, *args):
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.writeBuffer{tuple(args)} -> method')

    def fn_writeTexture(self, *args):
        logger.debug(f'patch -> v8_gpu_queue.py -> GPUQueue.writeTexture{tuple(args)} -> method')
