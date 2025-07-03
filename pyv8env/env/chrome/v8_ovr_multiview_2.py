from .flags import *


@construct_000000
class OVRMultiview2:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR = 38448
    FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR = 38450
    MAX_VIEWS_OVR = 38449
    FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR = 38451

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("framebufferTextureMultiviewOVR", "fn_framebufferTextureMultiviewOVR", 6, 0, 1, 0, 0, 0, 0),

    )

    def fn_framebufferTextureMultiviewOVR(self, *args):
        logger.debug(f'patch -> v8_ovr_multiview_2.py -> OVRMultiview2.framebufferTextureMultiviewOVR{tuple(args)} -> method')
