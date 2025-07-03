from .flags import *
from .v8_ui_event import UIEvent


@construct_111001
class MouseEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MouseEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("screenX", "get_screenX", None, 0, 1, 0, 0, 0, 0, 1),
        ("screenY", "get_screenY", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientX", "get_clientX", None, 0, 1, 0, 0, 0, 0, 1),
        ("clientY", "get_clientY", None, 0, 1, 0, 0, 0, 0, 1),
        ("ctrlKey", "get_ctrlKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("shiftKey", "get_shiftKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("altKey", "get_altKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("metaKey", "get_metaKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("button", "get_button", None, 0, 1, 0, 0, 0, 0, 1),
        ("buttons", "get_buttons", None, 0, 1, 0, 0, 0, 0, 1),
        ("relatedTarget", "get_relatedTarget", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageX", "get_pageX", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageY", "get_pageY", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("offsetX", "get_offsetX", None, 0, 1, 0, 0, 0, 0, 1),
        ("offsetY", "get_offsetY", None, 0, 1, 0, 0, 0, 0, 1),
        ("movementX", "get_movementX", None, 0, 1, 0, 0, 0, 0, 1),
        ("movementY", "get_movementY", None, 0, 1, 0, 0, 0, 0, 1),
        ("fromElement", "get_fromElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("toElement", "get_toElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("layerX", "get_layerX", None, 0, 1, 0, 0, 0, 0, 1),
        ("layerY", "get_layerY", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getModifierState", "fn_getModifierState", 1, 0, 1, 0, 0, 0, 0),
        ("initMouseEvent", "fn_initMouseEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_screenX(self):
        val = self._attr.get('screenX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.screenX -> get attr')

    def get_screenY(self):
        val = self._attr.get('screenY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.screenY -> get attr')

    def get_clientX(self):
        val = self._attr.get('clientX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.clientX -> get attr')

    def get_clientY(self):
        val = self._attr.get('clientY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.clientY -> get attr')

    def get_ctrlKey(self):
        val = self._attr.get('ctrlKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.ctrlKey -> get attr')

    def get_shiftKey(self):
        val = self._attr.get('shiftKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.shiftKey -> get attr')

    def get_altKey(self):
        val = self._attr.get('altKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.altKey -> get attr')

    def get_metaKey(self):
        val = self._attr.get('metaKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.metaKey -> get attr')

    def get_button(self):
        val = self._attr.get('button')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.button -> get attr')

    def get_buttons(self):
        val = self._attr.get('buttons')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.buttons -> get attr')

    def get_relatedTarget(self):
        val = self._attr.get('relatedTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.relatedTarget -> get attr')

    def get_pageX(self):
        val = self._attr.get('pageX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.pageX -> get attr')

    def get_pageY(self):
        val = self._attr.get('pageY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.pageY -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.y -> get attr')

    def get_offsetX(self):
        val = self._attr.get('offsetX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.offsetX -> get attr')

    def get_offsetY(self):
        val = self._attr.get('offsetY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.offsetY -> get attr')

    def get_movementX(self):
        val = self._attr.get('movementX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.movementX -> get attr')

    def get_movementY(self):
        val = self._attr.get('movementY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.movementY -> get attr')

    def get_fromElement(self):
        val = self._attr.get('fromElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.fromElement -> get attr')

    def get_toElement(self):
        val = self._attr.get('toElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.toElement -> get attr')

    def get_layerX(self):
        val = self._attr.get('layerX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.layerX -> get attr')

    def get_layerY(self):
        val = self._attr.get('layerY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.layerY -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.isTrusted -> get attr')

    def fn_getModifierState(self, *args):
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.getModifierState{tuple(args)} -> method')

    def fn_initMouseEvent(self, *args):
        logger.debug(f'patch -> v8_mouse_event.py -> MouseEvent.initMouseEvent{tuple(args)} -> method')
