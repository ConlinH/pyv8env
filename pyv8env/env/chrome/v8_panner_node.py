from .flags import *
from .v8_audio_node import AudioNode


@construct_111001
class PannerNode(AudioNode):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PannerNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("panningModel", "get_panningModel", "set_panningModel", 0, 1, 0, 0, 0, 0, 1),
        ("positionX", "get_positionX", None, 0, 1, 0, 0, 0, 0, 1),
        ("positionY", "get_positionY", None, 0, 1, 0, 0, 0, 0, 1),
        ("positionZ", "get_positionZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientationX", "get_orientationX", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientationY", "get_orientationY", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientationZ", "get_orientationZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("distanceModel", "get_distanceModel", "set_distanceModel", 0, 1, 0, 0, 0, 0, 1),
        ("refDistance", "get_refDistance", "set_refDistance", 0, 1, 0, 0, 0, 0, 1),
        ("maxDistance", "get_maxDistance", "set_maxDistance", 0, 1, 0, 0, 0, 0, 1),
        ("rolloffFactor", "get_rolloffFactor", "set_rolloffFactor", 0, 1, 0, 0, 0, 0, 1),
        ("coneInnerAngle", "get_coneInnerAngle", "set_coneInnerAngle", 0, 1, 0, 0, 0, 0, 1),
        ("coneOuterAngle", "get_coneOuterAngle", "set_coneOuterAngle", 0, 1, 0, 0, 0, 0, 1),
        ("coneOuterGain", "get_coneOuterGain", "set_coneOuterGain", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setOrientation", "fn_setOrientation", 3, 0, 1, 0, 0, 0, 0),
        ("setPosition", "fn_setPosition", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_panningModel(self):
        val = self._attr.get('panningModel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.panningModel -> get attr')

    def set_panningModel(self, val):
        self._attr['panningModel'] = val

    def get_positionX(self):
        val = self._attr.get('positionX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.positionX -> get attr')

    def get_positionY(self):
        val = self._attr.get('positionY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.positionY -> get attr')

    def get_positionZ(self):
        val = self._attr.get('positionZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.positionZ -> get attr')

    def get_orientationX(self):
        val = self._attr.get('orientationX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.orientationX -> get attr')

    def get_orientationY(self):
        val = self._attr.get('orientationY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.orientationY -> get attr')

    def get_orientationZ(self):
        val = self._attr.get('orientationZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.orientationZ -> get attr')

    def get_distanceModel(self):
        val = self._attr.get('distanceModel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.distanceModel -> get attr')

    def set_distanceModel(self, val):
        self._attr['distanceModel'] = val

    def get_refDistance(self):
        val = self._attr.get('refDistance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.refDistance -> get attr')

    def set_refDistance(self, val):
        self._attr['refDistance'] = val

    def get_maxDistance(self):
        val = self._attr.get('maxDistance')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.maxDistance -> get attr')

    def set_maxDistance(self, val):
        self._attr['maxDistance'] = val

    def get_rolloffFactor(self):
        val = self._attr.get('rolloffFactor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.rolloffFactor -> get attr')

    def set_rolloffFactor(self, val):
        self._attr['rolloffFactor'] = val

    def get_coneInnerAngle(self):
        val = self._attr.get('coneInnerAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.coneInnerAngle -> get attr')

    def set_coneInnerAngle(self, val):
        self._attr['coneInnerAngle'] = val

    def get_coneOuterAngle(self):
        val = self._attr.get('coneOuterAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.coneOuterAngle -> get attr')

    def set_coneOuterAngle(self, val):
        self._attr['coneOuterAngle'] = val

    def get_coneOuterGain(self):
        val = self._attr.get('coneOuterGain')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.coneOuterGain -> get attr')

    def set_coneOuterGain(self, val):
        self._attr['coneOuterGain'] = val

    def fn_setOrientation(self, *args):
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.setOrientation{tuple(args)} -> method')

    def fn_setPosition(self, *args):
        logger.debug(f'patch -> v8_panner_node.py -> PannerNode.setPosition{tuple(args)} -> method')
