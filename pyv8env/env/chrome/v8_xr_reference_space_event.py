from .flags import *
from .v8_event import Event


@construct_112001
class XRReferenceSpaceEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRReferenceSpaceEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("referenceSpace", "get_referenceSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("transform", "get_transform", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_referenceSpace(self):
        val = self._attr.get('referenceSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_reference_space_event.py -> XRReferenceSpaceEvent.referenceSpace -> get attr')

    def get_transform(self):
        val = self._attr.get('transform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_reference_space_event.py -> XRReferenceSpaceEvent.transform -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_reference_space_event.py -> XRReferenceSpaceEvent.isTrusted -> get attr')
