from .flags import *


@construct_000000
class PagePopupController:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("closePopup", "fn_closePopup", 0, 0, 1, 0, 0, 0, 0),
        ("formatMonth", "fn_formatMonth", 2, 0, 1, 0, 0, 0, 0),
        ("formatShortMonth", "fn_formatShortMonth", 2, 0, 1, 0, 0, 0, 0),
        ("formatWeek", "fn_formatWeek", 3, 0, 1, 0, 0, 0, 0),
        ("localizeNumberString", "fn_localizeNumberString", 1, 0, 1, 0, 0, 0, 0),
        ("setMenuListOptionsBoundsInAXTree", "fn_setMenuListOptionsBoundsInAXTree", 1, 0, 1, 0, 0, 0, 0),
        ("setValue", "fn_setValue", 1, 0, 1, 0, 0, 0, 0),
        ("setValueAndClosePopup", "fn_setValueAndClosePopup", 2, 0, 1, 0, 0, 0, 0),
        ("setWindowRect", "fn_setWindowRect", 4, 0, 1, 0, 0, 0, 0),

    )

    def fn_closePopup(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.closePopup{tuple(args)} -> method')

    def fn_formatMonth(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.formatMonth{tuple(args)} -> method')

    def fn_formatShortMonth(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.formatShortMonth{tuple(args)} -> method')

    def fn_formatWeek(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.formatWeek{tuple(args)} -> method')

    def fn_localizeNumberString(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.localizeNumberString{tuple(args)} -> method')

    def fn_setMenuListOptionsBoundsInAXTree(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.setMenuListOptionsBoundsInAXTree{tuple(args)} -> method')

    def fn_setValue(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.setValue{tuple(args)} -> method')

    def fn_setValueAndClosePopup(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.setValueAndClosePopup{tuple(args)} -> method')

    def fn_setWindowRect(self, *args):
        logger.debug(f'patch -> v8_page_popup_controller.py -> PagePopupController.setWindowRect{tuple(args)} -> method')
