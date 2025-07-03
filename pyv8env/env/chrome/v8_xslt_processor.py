from .flags import *


@construct_110001
class XSLTProcessor:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearParameters", "fn_clearParameters", 0, 0, 1, 0, 0, 0, 0),
        ("getParameter", "fn_getParameter", 2, 0, 1, 0, 0, 0, 0),
        ("importStylesheet", "fn_importStylesheet", 1, 0, 1, 0, 0, 0, 0),
        ("removeParameter", "fn_removeParameter", 2, 0, 1, 0, 0, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("setParameter", "fn_setParameter", 3, 0, 1, 0, 0, 0, 0),
        ("transformToDocument", "fn_transformToDocument", 1, 0, 1, 0, 0, 0, 0),
        ("transformToFragment", "fn_transformToFragment", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_clearParameters(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.clearParameters{tuple(args)} -> method')

    def fn_getParameter(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.getParameter{tuple(args)} -> method')

    def fn_importStylesheet(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.importStylesheet{tuple(args)} -> method')

    def fn_removeParameter(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.removeParameter{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.reset{tuple(args)} -> method')

    def fn_setParameter(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.setParameter{tuple(args)} -> method')

    def fn_transformToDocument(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.transformToDocument{tuple(args)} -> method')

    def fn_transformToFragment(self, *args):
        logger.debug(f'patch -> v8_xslt_processor.py -> XSLTProcessor.transformToFragment{tuple(args)} -> method')
