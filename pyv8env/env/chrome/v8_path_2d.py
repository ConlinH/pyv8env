from .flags import *


@construct_110001
class Path2D:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addPath", "fn_addPath", 1, 0, 1, 0, 0, 0, 0),
        ("roundRect", "fn_roundRect", 4, 0, 1, 0, 0, 0, 0),
        ("arc", "fn_arc", 5, 0, 1, 0, 0, 0, 0),
        ("arcTo", "fn_arcTo", 5, 0, 1, 0, 0, 0, 0),
        ("bezierCurveTo", "fn_bezierCurveTo", 6, 0, 1, 0, 0, 0, 0),
        ("closePath", "fn_closePath", 0, 0, 1, 0, 0, 0, 0),
        ("ellipse", "fn_ellipse", 7, 0, 1, 0, 0, 0, 0),
        ("lineTo", "fn_lineTo", 2, 0, 1, 0, 0, 0, 0),
        ("moveTo", "fn_moveTo", 2, 0, 1, 0, 0, 0, 0),
        ("quadraticCurveTo", "fn_quadraticCurveTo", 4, 0, 1, 0, 0, 0, 0),
        ("rect", "fn_rect", 4, 0, 1, 0, 0, 0, 0),

    )

    def fn_addPath(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.addPath{tuple(args)} -> method')

    def fn_roundRect(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.roundRect{tuple(args)} -> method')

    def fn_arc(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.arc{tuple(args)} -> method')

    def fn_arcTo(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.arcTo{tuple(args)} -> method')

    def fn_bezierCurveTo(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.bezierCurveTo{tuple(args)} -> method')

    def fn_closePath(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.closePath{tuple(args)} -> method')

    def fn_ellipse(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.ellipse{tuple(args)} -> method')

    def fn_lineTo(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.lineTo{tuple(args)} -> method')

    def fn_moveTo(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.moveTo{tuple(args)} -> method')

    def fn_quadraticCurveTo(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.quadraticCurveTo{tuple(args)} -> method')

    def fn_rect(self, *args):
        logger.debug(f'patch -> v8_path_2d.py -> Path2D.rect{tuple(args)} -> method')
