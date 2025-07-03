from .flags import *


@construct_100001
class PaintRenderingContext2D:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("globalAlpha", "get_globalAlpha", "set_globalAlpha", 0, 1, 0, 0, 0, 0, 1),
        ("globalCompositeOperation", "get_globalCompositeOperation", "set_globalCompositeOperation", 0, 1, 0, 0, 0, 0, 1),
        ("filter", "get_filter", "set_filter", 0, 1, 0, 0, 0, 0, 1),
        ("imageSmoothingEnabled", "get_imageSmoothingEnabled", "set_imageSmoothingEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("strokeStyle", "get_strokeStyle", "set_strokeStyle", 0, 1, 0, 0, 0, 0, 1),
        ("fillStyle", "get_fillStyle", "set_fillStyle", 0, 1, 0, 0, 0, 0, 1),
        ("shadowOffsetX", "get_shadowOffsetX", "set_shadowOffsetX", 0, 1, 0, 0, 0, 0, 1),
        ("shadowOffsetY", "get_shadowOffsetY", "set_shadowOffsetY", 0, 1, 0, 0, 0, 0, 1),
        ("shadowBlur", "get_shadowBlur", "set_shadowBlur", 0, 1, 0, 0, 0, 0, 1),
        ("shadowColor", "get_shadowColor", "set_shadowColor", 0, 1, 0, 0, 0, 0, 1),
        ("lineWidth", "get_lineWidth", "set_lineWidth", 0, 1, 0, 0, 0, 0, 1),
        ("lineCap", "get_lineCap", "set_lineCap", 0, 1, 0, 0, 0, 0, 1),
        ("lineJoin", "get_lineJoin", "set_lineJoin", 0, 1, 0, 0, 0, 0, 1),
        ("miterLimit", "get_miterLimit", "set_miterLimit", 0, 1, 0, 0, 0, 0, 1),
        ("lineDashOffset", "get_lineDashOffset", "set_lineDashOffset", 0, 1, 0, 0, 0, 0, 1),
        ("imageSmoothingQuality", "get_imageSmoothingQuality", "set_imageSmoothingQuality", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("beginPath", "fn_beginPath", 0, 0, 1, 0, 0, 0, 0),
        ("clearRect", "fn_clearRect", 4, 0, 1, 0, 0, 0, 0),
        ("clip", "fn_clip", 0, 0, 1, 0, 0, 0, 0),
        ("createConicGradient", "fn_createConicGradient", 3, 0, 1, 0, 0, 0, 0),
        ("createLinearGradient", "fn_createLinearGradient", 4, 0, 1, 0, 0, 0, 0),
        ("createPattern", "fn_createPattern", 2, 0, 1, 0, 0, 0, 0),
        ("createRadialGradient", "fn_createRadialGradient", 6, 0, 1, 0, 0, 0, 0),
        ("drawImage", "fn_drawImage", 3, 0, 1, 0, 0, 0, 0),
        ("fill", "fn_fill", 0, 0, 1, 0, 0, 0, 0),
        ("fillRect", "fn_fillRect", 4, 0, 1, 0, 0, 0, 0),
        ("getLineDash", "fn_getLineDash", 0, 0, 1, 0, 0, 0, 0),
        ("getTransform", "fn_getTransform", 0, 0, 1, 0, 0, 0, 0),
        ("isPointInPath", "fn_isPointInPath", 2, 0, 1, 0, 0, 0, 0),
        ("isPointInStroke", "fn_isPointInStroke", 2, 0, 1, 0, 0, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 0, 0, 0),
        ("resetTransform", "fn_resetTransform", 0, 0, 1, 0, 0, 0, 0),
        ("restore", "fn_restore", 0, 0, 1, 0, 0, 0, 0),
        ("rotate", "fn_rotate", 1, 0, 1, 0, 0, 0, 0),
        ("roundRect", "fn_roundRect", 4, 0, 1, 0, 0, 0, 0),
        ("save", "fn_save", 0, 0, 1, 0, 0, 0, 0),
        ("scale", "fn_scale", 2, 0, 1, 0, 0, 0, 0),
        ("setLineDash", "fn_setLineDash", 1, 0, 1, 0, 0, 0, 0),
        ("setTransform", "fn_setTransform", 0, 0, 1, 0, 0, 0, 0),
        ("stroke", "fn_stroke", 0, 0, 1, 0, 0, 0, 0),
        ("strokeRect", "fn_strokeRect", 4, 0, 1, 0, 0, 0, 0),
        ("transform", "fn_transform", 6, 0, 1, 0, 0, 0, 0),
        ("translate", "fn_translate", 2, 0, 1, 0, 0, 0, 0),
        ("beginLayer", "fn_beginLayer", 0, 0, 1, 0, 0, 0, 0),
        ("endLayer", "fn_endLayer", 0, 0, 1, 0, 0, 0, 0),
        ("createMesh2DIndexBuffer", "fn_createMesh2DIndexBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("createMesh2DUVBuffer", "fn_createMesh2DUVBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("createMesh2DVertexBuffer", "fn_createMesh2DVertexBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("drawMesh", "fn_drawMesh", 4, 0, 1, 0, 0, 0, 0),
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

    def get_globalAlpha(self):
        val = self._attr.get('globalAlpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.globalAlpha -> get attr')

    def set_globalAlpha(self, val):
        self._attr['globalAlpha'] = val

    def get_globalCompositeOperation(self):
        val = self._attr.get('globalCompositeOperation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.globalCompositeOperation -> get attr')

    def set_globalCompositeOperation(self, val):
        self._attr['globalCompositeOperation'] = val

    def get_filter(self):
        val = self._attr.get('filter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.filter -> get attr')

    def set_filter(self, val):
        self._attr['filter'] = val

    def get_imageSmoothingEnabled(self):
        val = self._attr.get('imageSmoothingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.imageSmoothingEnabled -> get attr')

    def set_imageSmoothingEnabled(self, val):
        self._attr['imageSmoothingEnabled'] = val

    def get_strokeStyle(self):
        val = self._attr.get('strokeStyle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.strokeStyle -> get attr')

    def set_strokeStyle(self, val):
        self._attr['strokeStyle'] = val

    def get_fillStyle(self):
        val = self._attr.get('fillStyle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.fillStyle -> get attr')

    def set_fillStyle(self, val):
        self._attr['fillStyle'] = val

    def get_shadowOffsetX(self):
        val = self._attr.get('shadowOffsetX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.shadowOffsetX -> get attr')

    def set_shadowOffsetX(self, val):
        self._attr['shadowOffsetX'] = val

    def get_shadowOffsetY(self):
        val = self._attr.get('shadowOffsetY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.shadowOffsetY -> get attr')

    def set_shadowOffsetY(self, val):
        self._attr['shadowOffsetY'] = val

    def get_shadowBlur(self):
        val = self._attr.get('shadowBlur')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.shadowBlur -> get attr')

    def set_shadowBlur(self, val):
        self._attr['shadowBlur'] = val

    def get_shadowColor(self):
        val = self._attr.get('shadowColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.shadowColor -> get attr')

    def set_shadowColor(self, val):
        self._attr['shadowColor'] = val

    def get_lineWidth(self):
        val = self._attr.get('lineWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.lineWidth -> get attr')

    def set_lineWidth(self, val):
        self._attr['lineWidth'] = val

    def get_lineCap(self):
        val = self._attr.get('lineCap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.lineCap -> get attr')

    def set_lineCap(self, val):
        self._attr['lineCap'] = val

    def get_lineJoin(self):
        val = self._attr.get('lineJoin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.lineJoin -> get attr')

    def set_lineJoin(self, val):
        self._attr['lineJoin'] = val

    def get_miterLimit(self):
        val = self._attr.get('miterLimit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.miterLimit -> get attr')

    def set_miterLimit(self, val):
        self._attr['miterLimit'] = val

    def get_lineDashOffset(self):
        val = self._attr.get('lineDashOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.lineDashOffset -> get attr')

    def set_lineDashOffset(self, val):
        self._attr['lineDashOffset'] = val

    def get_imageSmoothingQuality(self):
        val = self._attr.get('imageSmoothingQuality')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.imageSmoothingQuality -> get attr')

    def set_imageSmoothingQuality(self, val):
        self._attr['imageSmoothingQuality'] = val

    def fn_beginPath(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.beginPath{tuple(args)} -> method')

    def fn_clearRect(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.clearRect{tuple(args)} -> method')

    def fn_clip(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.clip{tuple(args)} -> method')

    def fn_createConicGradient(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createConicGradient{tuple(args)} -> method')

    def fn_createLinearGradient(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createLinearGradient{tuple(args)} -> method')

    def fn_createPattern(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createPattern{tuple(args)} -> method')

    def fn_createRadialGradient(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createRadialGradient{tuple(args)} -> method')

    def fn_drawImage(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.drawImage{tuple(args)} -> method')

    def fn_fill(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.fill{tuple(args)} -> method')

    def fn_fillRect(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.fillRect{tuple(args)} -> method')

    def fn_getLineDash(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.getLineDash{tuple(args)} -> method')

    def fn_getTransform(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.getTransform{tuple(args)} -> method')

    def fn_isPointInPath(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.isPointInPath{tuple(args)} -> method')

    def fn_isPointInStroke(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.isPointInStroke{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.reset{tuple(args)} -> method')

    def fn_resetTransform(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.resetTransform{tuple(args)} -> method')

    def fn_restore(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.restore{tuple(args)} -> method')

    def fn_rotate(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.rotate{tuple(args)} -> method')

    def fn_roundRect(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.roundRect{tuple(args)} -> method')

    def fn_save(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.save{tuple(args)} -> method')

    def fn_scale(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.scale{tuple(args)} -> method')

    def fn_setLineDash(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.setLineDash{tuple(args)} -> method')

    def fn_setTransform(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.setTransform{tuple(args)} -> method')

    def fn_stroke(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.stroke{tuple(args)} -> method')

    def fn_strokeRect(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.strokeRect{tuple(args)} -> method')

    def fn_transform(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.transform{tuple(args)} -> method')

    def fn_translate(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.translate{tuple(args)} -> method')

    def fn_beginLayer(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.beginLayer{tuple(args)} -> method')

    def fn_endLayer(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.endLayer{tuple(args)} -> method')

    def fn_createMesh2DIndexBuffer(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createMesh2DIndexBuffer{tuple(args)} -> method')

    def fn_createMesh2DUVBuffer(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createMesh2DUVBuffer{tuple(args)} -> method')

    def fn_createMesh2DVertexBuffer(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.createMesh2DVertexBuffer{tuple(args)} -> method')

    def fn_drawMesh(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.drawMesh{tuple(args)} -> method')

    def fn_arc(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.arc{tuple(args)} -> method')

    def fn_arcTo(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.arcTo{tuple(args)} -> method')

    def fn_bezierCurveTo(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.bezierCurveTo{tuple(args)} -> method')

    def fn_closePath(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.closePath{tuple(args)} -> method')

    def fn_ellipse(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.ellipse{tuple(args)} -> method')

    def fn_lineTo(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.lineTo{tuple(args)} -> method')

    def fn_moveTo(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.moveTo{tuple(args)} -> method')

    def fn_quadraticCurveTo(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.quadraticCurveTo{tuple(args)} -> method')

    def fn_rect(self, *args):
        logger.debug(f'patch -> v8_paint_rendering_context_2d.py -> PaintRenderingContext2D.rect{tuple(args)} -> method')
