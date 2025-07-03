from .flags import *


@construct_100001
class XRFrame:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("session", "get_session", None, 0, 1, 0, 0, 0, 0, 1),
        ("trackedAnchors", "get_trackedAnchors", None, 0, 1, 0, 0, 0, 0, 1),
        ("detectedPlanes", "get_detectedPlanes", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPose", "fn_getPose", 2, 0, 1, 0, 0, 0, 0),
        ("getViewerPose", "fn_getViewerPose", 1, 0, 1, 0, 0, 0, 0),
        ("createAnchor", "fn_createAnchor", 2, 0, 1, 0, 1, 0, 0),
        ("getDepthInformation", "fn_getDepthInformation", 1, 0, 1, 0, 0, 0, 0),
        ("getHitTestResults", "fn_getHitTestResults", 1, 0, 1, 0, 0, 0, 0),
        ("getHitTestResultsForTransientInput", "fn_getHitTestResultsForTransientInput", 1, 0, 1, 0, 0, 0, 0),
        ("getLightEstimate", "fn_getLightEstimate", 1, 0, 1, 0, 0, 0, 0),
        ("fillJointRadii", "fn_fillJointRadii", 2, 0, 1, 0, 0, 0, 0),
        ("fillPoses", "fn_fillPoses", 3, 0, 1, 0, 0, 0, 0),
        ("getJointPose", "fn_getJointPose", 2, 0, 1, 0, 0, 0, 0),
        ("getImageTrackingResults", "fn_getImageTrackingResults", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_session(self):
        val = self._attr.get('session')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.session -> get attr')

    def get_trackedAnchors(self):
        val = self._attr.get('trackedAnchors')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.trackedAnchors -> get attr')

    def get_detectedPlanes(self):
        val = self._attr.get('detectedPlanes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.detectedPlanes -> get attr')

    def fn_getPose(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getPose{tuple(args)} -> method')

    def fn_getViewerPose(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getViewerPose{tuple(args)} -> method')

    def fn_createAnchor(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.createAnchor{tuple(args)} -> method')

    def fn_getDepthInformation(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getDepthInformation{tuple(args)} -> method')

    def fn_getHitTestResults(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getHitTestResults{tuple(args)} -> method')

    def fn_getHitTestResultsForTransientInput(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getHitTestResultsForTransientInput{tuple(args)} -> method')

    def fn_getLightEstimate(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getLightEstimate{tuple(args)} -> method')

    def fn_fillJointRadii(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.fillJointRadii{tuple(args)} -> method')

    def fn_fillPoses(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.fillPoses{tuple(args)} -> method')

    def fn_getJointPose(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getJointPose{tuple(args)} -> method')

    def fn_getImageTrackingResults(self, *args):
        logger.debug(f'patch -> v8_xr_frame.py -> XRFrame.getImageTrackingResults{tuple(args)} -> method')
