from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class DynamicsCompressorNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DynamicsCompressorNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("threshold", "get_threshold", None, 0, 1, 0, 0, 0, 0, 1),
        ("knee", "get_knee", None, 0, 1, 0, 0, 0, 0, 1),
        ("ratio", "get_ratio", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduction", "get_reduction", None, 0, 1, 0, 0, 0, 0, 1),
        ("attack", "get_attack", None, 0, 1, 0, 0, 0, 0, 1),
        ("release", "get_release", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_threshold(self):
        val = self._attr.get('threshold')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.threshold -> get attr')

    def get_knee(self):
        val = self._attr.get('knee')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.knee -> get attr')

    def get_ratio(self):
        val = self._attr.get('ratio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.ratio -> get attr')

    def get_reduction(self):
        val = self._attr.get('reduction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.reduction -> get attr')

    def get_attack(self):
        val = self._attr.get('attack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.attack -> get attr')

    def get_release(self):
        val = self._attr.get('release')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_dynamics_compressor_node.py -> DynamicsCompressorNode.release -> get attr')
