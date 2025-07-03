from .flags import *


@construct_100001
class GPUCompilationMessage:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNum", "get_lineNum", None, 0, 1, 0, 0, 0, 0, 1),
        ("linePos", "get_linePos", None, 0, 1, 0, 0, 0, 0, 1),
        ("offset", "get_offset", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.message -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.type -> get attr')

    def get_lineNum(self):
        val = self._attr.get('lineNum')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.lineNum -> get attr')

    def get_linePos(self):
        val = self._attr.get('linePos')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.linePos -> get attr')

    def get_offset(self):
        val = self._attr.get('offset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.offset -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_compilation_message.py -> GPUCompilationMessage.length -> get attr')
