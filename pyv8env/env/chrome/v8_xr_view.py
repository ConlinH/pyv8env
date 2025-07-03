from .flags import *


@construct_100001
class XRView:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("eye", "get_eye", None, 0, 1, 0, 0, 0, 0, 1),
        ("projectionMatrix", "get_projectionMatrix", None, 0, 1, 0, 0, 0, 0, 1),
        ("transform", "get_transform", None, 0, 1, 0, 0, 0, 0, 1),
        ("recommendedViewportScale", "get_recommendedViewportScale", None, 0, 1, 0, 0, 0, 0, 1),
        ("isFirstPersonObserver", "get_isFirstPersonObserver", None, 0, 1, 0, 0, 0, 0, 1),
        ("camera", "get_camera", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestViewportScale", "fn_requestViewportScale", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_eye(self):
        val = self._attr.get('eye')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.eye -> get attr')

    def get_projectionMatrix(self):
        val = self._attr.get('projectionMatrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.projectionMatrix -> get attr')

    def get_transform(self):
        val = self._attr.get('transform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.transform -> get attr')

    def get_recommendedViewportScale(self):
        val = self._attr.get('recommendedViewportScale')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.recommendedViewportScale -> get attr')

    def get_isFirstPersonObserver(self):
        val = self._attr.get('isFirstPersonObserver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.isFirstPersonObserver -> get attr')

    def get_camera(self):
        val = self._attr.get('camera')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_view.py -> XRView.camera -> get attr')

    def fn_requestViewportScale(self, *args):
        logger.debug(f'patch -> v8_xr_view.py -> XRView.requestViewportScale{tuple(args)} -> method')
