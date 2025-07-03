from .flags import *
from .v8_document_fragment import DocumentFragment


@construct_100001
class ShadowRoot(DocumentFragment):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ShadowRoot, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("mode", "get_mode", None, 0, 1, 0, 0, 0, 0, 1),
        ("host", "get_host", None, 0, 1, 0, 0, 0, 0, 1),
        ("onslotchange", "get_onslotchange", "set_onslotchange", 0, 1, 0, 0, 0, 0, 1),
        ("innerHTML", "get_innerHTML", "set_innerHTML", 0, 1, 0, 0, 0, 0, 1),
        ("delegatesFocus", "get_delegatesFocus", None, 0, 1, 0, 0, 0, 0, 1),
        ("slotAssignment", "get_slotAssignment", None, 0, 1, 0, 0, 0, 0, 1),
        ("serializable", "get_serializable", None, 0, 1, 0, 0, 0, 0, 1),
        ("clonable", "get_clonable", None, 0, 1, 0, 0, 0, 0, 1),
        ("activeElement", "get_activeElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("styleSheets", "get_styleSheets", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerLockElement", "get_pointerLockElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullscreenElement", "get_fullscreenElement", "set_fullscreenElement", 0, 1, 0, 0, 0, 0, 1),
        ("adoptedStyleSheets", "get_adoptedStyleSheets", "set_adoptedStyleSheets", 0, 1, 0, 0, 0, 0, 1),
        ("pictureInPictureElement", "get_pictureInPictureElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("registry", "get_registry", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("elementFromPoint", "fn_elementFromPoint", 2, 0, 1, 0, 0, 0, 0),
        ("elementsFromPoint", "fn_elementsFromPoint", 2, 0, 1, 0, 0, 0, 0),
        ("getAnimations", "fn_getAnimations", 0, 0, 1, 0, 0, 0, 0),
        ("getHTML", "fn_getHTML", 0, 0, 1, 0, 0, 0, 1),
        ("getSelection", "fn_getSelection", 0, 0, 1, 0, 0, 0, 1),
        ("createElement", "fn_createElement", 1, 0, 1, 0, 0, 0, 0),
        ("createElementNS", "fn_createElementNS", 2, 0, 1, 0, 0, 0, 0),
        ("getInnerHTML", "fn_getInnerHTML", 0, 0, 1, 0, 0, 0, 1),
        ("setHTMLUnsafe", "fn_setHTMLUnsafe", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_mode(self):
        val = self._attr.get('mode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.mode -> get attr')

    def get_host(self):
        val = self._attr.get('host')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.host -> get attr')

    def get_onslotchange(self):
        val = self._attr.get('onslotchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.onslotchange -> get attr')

    def set_onslotchange(self, val):
        self._attr['onslotchange'] = val

    def get_innerHTML(self):
        val = self._attr.get('innerHTML')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.innerHTML -> get attr')

    def set_innerHTML(self, val):
        self._attr['innerHTML'] = val

    def get_delegatesFocus(self):
        val = self._attr.get('delegatesFocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.delegatesFocus -> get attr')

    def get_slotAssignment(self):
        val = self._attr.get('slotAssignment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.slotAssignment -> get attr')

    def get_serializable(self):
        val = self._attr.get('serializable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.serializable -> get attr')

    def get_clonable(self):
        val = self._attr.get('clonable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.clonable -> get attr')

    def get_activeElement(self):
        val = self._attr.get('activeElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.activeElement -> get attr')

    def get_styleSheets(self):
        val = self._attr.get('styleSheets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.styleSheets -> get attr')

    def get_pointerLockElement(self):
        val = self._attr.get('pointerLockElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.pointerLockElement -> get attr')

    def get_fullscreenElement(self):
        val = self._attr.get('fullscreenElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.fullscreenElement -> get attr')

    def set_fullscreenElement(self, val):
        self._attr['fullscreenElement'] = val

    def get_adoptedStyleSheets(self):
        val = self._attr.get('adoptedStyleSheets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.adoptedStyleSheets -> get attr')

    def set_adoptedStyleSheets(self, val):
        self._attr['adoptedStyleSheets'] = val

    def get_pictureInPictureElement(self):
        val = self._attr.get('pictureInPictureElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.pictureInPictureElement -> get attr')

    def get_registry(self):
        val = self._attr.get('registry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.registry -> get attr')

    def fn_elementFromPoint(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.elementFromPoint{tuple(args)} -> method')

    def fn_elementsFromPoint(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.elementsFromPoint{tuple(args)} -> method')

    def fn_getAnimations(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.getAnimations{tuple(args)} -> method')

    def fn_getHTML(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.getHTML{tuple(args)} -> method')

    def fn_getSelection(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.getSelection{tuple(args)} -> method')

    def fn_createElement(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.createElement{tuple(args)} -> method')

    def fn_createElementNS(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.createElementNS{tuple(args)} -> method')

    def fn_getInnerHTML(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.getInnerHTML{tuple(args)} -> method')

    def fn_setHTMLUnsafe(self, *args):
        logger.debug(f'patch -> v8_shadow_root.py -> ShadowRoot.setHTMLUnsafe{tuple(args)} -> method')
