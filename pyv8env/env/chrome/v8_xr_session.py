from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class XRSession(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(XRSession, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("environmentBlendMode", "get_environmentBlendMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("interactionMode", "get_interactionMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibilityState", "get_visibilityState", None, 0, 1, 0, 0, 0, 0, 1),
        ("renderState", "get_renderState", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputSources", "get_inputSources", None, 0, 1, 0, 0, 0, 0, 1),
        ("domOverlayState", "get_domOverlayState", None, 0, 1, 0, 0, 0, 0, 1),
        ("preferredReflectionFormat", "get_preferredReflectionFormat", None, 0, 1, 0, 0, 0, 0, 1),
        ("onend", "get_onend", "set_onend", 0, 1, 0, 0, 0, 0, 1),
        ("onselect", "get_onselect", "set_onselect", 0, 1, 0, 0, 0, 0, 1),
        ("oninputsourceschange", "get_oninputsourceschange", "set_oninputsourceschange", 0, 1, 0, 0, 0, 0, 1),
        ("onselectstart", "get_onselectstart", "set_onselectstart", 0, 1, 0, 0, 0, 0, 1),
        ("onselectend", "get_onselectend", "set_onselectend", 0, 1, 0, 0, 0, 0, 1),
        ("onvisibilitychange", "get_onvisibilitychange", "set_onvisibilitychange", 0, 1, 0, 0, 0, 0, 1),
        ("onsqueeze", "get_onsqueeze", "set_onsqueeze", 0, 1, 0, 0, 0, 0, 1),
        ("onsqueezestart", "get_onsqueezestart", "set_onsqueezestart", 0, 1, 0, 0, 0, 0, 1),
        ("onsqueezeend", "get_onsqueezeend", "set_onsqueezeend", 0, 1, 0, 0, 0, 0, 1),
        ("depthUsage", "get_depthUsage", None, 0, 1, 0, 0, 0, 0, 1),
        ("depthDataFormat", "get_depthDataFormat", None, 0, 1, 0, 0, 0, 0, 1),
        ("frameRate", "get_frameRate", None, 0, 1, 0, 0, 0, 0, 1),
        ("supportedFrameRates", "get_supportedFrameRates", None, 0, 1, 0, 0, 0, 0, 1),
        ("onframeratechange", "get_onframeratechange", "set_onframeratechange", 0, 1, 0, 0, 0, 0, 1),
        ("enabledFeatures", "get_enabledFeatures", None, 0, 1, 0, 0, 0, 0, 1),
        ("isSystemKeyboardSupported", "get_isSystemKeyboardSupported", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancelAnimationFrame", "fn_cancelAnimationFrame", 1, 0, 1, 0, 0, 0, 0),
        ("end", "fn_end", 0, 0, 1, 0, 1, 0, 0),
        ("requestAnimationFrame", "fn_requestAnimationFrame", 1, 0, 1, 0, 0, 0, 0),
        ("requestHitTestSource", "fn_requestHitTestSource", 1, 0, 1, 0, 1, 0, 0),
        ("requestHitTestSourceForTransientInput", "fn_requestHitTestSourceForTransientInput", 1, 0, 1, 0, 1, 0, 0),
        ("requestLightProbe", "fn_requestLightProbe", 0, 0, 1, 0, 1, 0, 0),
        ("requestReferenceSpace", "fn_requestReferenceSpace", 1, 0, 1, 0, 1, 0, 0),
        ("updateRenderState", "fn_updateRenderState", 0, 0, 1, 0, 0, 0, 0),
        ("updateTargetFrameRate", "fn_updateTargetFrameRate", 1, 0, 1, 0, 1, 0, 0),
        ("getTrackedImageScores", "fn_getTrackedImageScores", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_environmentBlendMode(self):
        val = self._attr.get('environmentBlendMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.environmentBlendMode -> get attr')

    def get_interactionMode(self):
        val = self._attr.get('interactionMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.interactionMode -> get attr')

    def get_visibilityState(self):
        val = self._attr.get('visibilityState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.visibilityState -> get attr')

    def get_renderState(self):
        val = self._attr.get('renderState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.renderState -> get attr')

    def get_inputSources(self):
        val = self._attr.get('inputSources')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.inputSources -> get attr')

    def get_domOverlayState(self):
        val = self._attr.get('domOverlayState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.domOverlayState -> get attr')

    def get_preferredReflectionFormat(self):
        val = self._attr.get('preferredReflectionFormat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.preferredReflectionFormat -> get attr')

    def get_onend(self):
        val = self._attr.get('onend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onend -> get attr')

    def set_onend(self, val):
        self._attr['onend'] = val

    def get_onselect(self):
        val = self._attr.get('onselect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onselect -> get attr')

    def set_onselect(self, val):
        self._attr['onselect'] = val

    def get_oninputsourceschange(self):
        val = self._attr.get('oninputsourceschange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.oninputsourceschange -> get attr')

    def set_oninputsourceschange(self, val):
        self._attr['oninputsourceschange'] = val

    def get_onselectstart(self):
        val = self._attr.get('onselectstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onselectstart -> get attr')

    def set_onselectstart(self, val):
        self._attr['onselectstart'] = val

    def get_onselectend(self):
        val = self._attr.get('onselectend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onselectend -> get attr')

    def set_onselectend(self, val):
        self._attr['onselectend'] = val

    def get_onvisibilitychange(self):
        val = self._attr.get('onvisibilitychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onvisibilitychange -> get attr')

    def set_onvisibilitychange(self, val):
        self._attr['onvisibilitychange'] = val

    def get_onsqueeze(self):
        val = self._attr.get('onsqueeze')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onsqueeze -> get attr')

    def set_onsqueeze(self, val):
        self._attr['onsqueeze'] = val

    def get_onsqueezestart(self):
        val = self._attr.get('onsqueezestart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onsqueezestart -> get attr')

    def set_onsqueezestart(self, val):
        self._attr['onsqueezestart'] = val

    def get_onsqueezeend(self):
        val = self._attr.get('onsqueezeend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onsqueezeend -> get attr')

    def set_onsqueezeend(self, val):
        self._attr['onsqueezeend'] = val

    def get_depthUsage(self):
        val = self._attr.get('depthUsage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.depthUsage -> get attr')

    def get_depthDataFormat(self):
        val = self._attr.get('depthDataFormat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.depthDataFormat -> get attr')

    def get_frameRate(self):
        val = self._attr.get('frameRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.frameRate -> get attr')

    def get_supportedFrameRates(self):
        val = self._attr.get('supportedFrameRates')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.supportedFrameRates -> get attr')

    def get_onframeratechange(self):
        val = self._attr.get('onframeratechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.onframeratechange -> get attr')

    def set_onframeratechange(self, val):
        self._attr['onframeratechange'] = val

    def get_enabledFeatures(self):
        val = self._attr.get('enabledFeatures')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.enabledFeatures -> get attr')

    def get_isSystemKeyboardSupported(self):
        val = self._attr.get('isSystemKeyboardSupported')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.isSystemKeyboardSupported -> get attr')

    def fn_cancelAnimationFrame(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.cancelAnimationFrame{tuple(args)} -> method')

    def fn_end(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.end{tuple(args)} -> method')

    def fn_requestAnimationFrame(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.requestAnimationFrame{tuple(args)} -> method')

    def fn_requestHitTestSource(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.requestHitTestSource{tuple(args)} -> method')

    def fn_requestHitTestSourceForTransientInput(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.requestHitTestSourceForTransientInput{tuple(args)} -> method')

    def fn_requestLightProbe(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.requestLightProbe{tuple(args)} -> method')

    def fn_requestReferenceSpace(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.requestReferenceSpace{tuple(args)} -> method')

    def fn_updateRenderState(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.updateRenderState{tuple(args)} -> method')

    def fn_updateTargetFrameRate(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.updateTargetFrameRate{tuple(args)} -> method')

    def fn_getTrackedImageScores(self, *args):
        logger.debug(f'patch -> v8_xr_session.py -> XRSession.getTrackedImageScores{tuple(args)} -> method')
