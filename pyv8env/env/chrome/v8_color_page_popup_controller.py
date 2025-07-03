from .flags import *
from .v8_page_popup_controller import PagePopupController


@construct_000000
class ColorPagePopupController(PagePopupController):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ColorPagePopupController, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("openEyeDropper", "fn_openEyeDropper", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_openEyeDropper(self, *args):
        logger.debug(f'patch -> v8_color_page_popup_controller.py -> ColorPagePopupController.openEyeDropper{tuple(args)} -> method')
