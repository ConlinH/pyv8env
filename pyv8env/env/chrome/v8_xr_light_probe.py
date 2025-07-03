from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class XRLightProbe(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRLightProbe, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("probeSpace", "get_probeSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("onreflectionchange", "get_onreflectionchange", "set_onreflectionchange", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_probeSpace(self):
        val = self._attr.get('probeSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_light_probe.py -> XRLightProbe.probeSpace -> get attr')

    def get_onreflectionchange(self):
        val = self._attr.get('onreflectionchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_light_probe.py -> XRLightProbe.onreflectionchange -> get attr')

    def set_onreflectionchange(self, val):
        self._attr['onreflectionchange'] = val
