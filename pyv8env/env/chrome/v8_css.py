from .flags import *


@construct_100001
class CSS:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("highlights", "get_highlights", None, 0, 2, 0, 1, 1, 1, 1),
        ("layoutWorklet", "get_layoutWorklet", None, 0, 2, 0, 1, 1, 1, 1),
        ("animationWorklet", "get_animationWorklet", None, 0, 2, 0, 1, 1, 1, 1),
        ("paintWorklet", "get_paintWorklet", None, 0, 2, 0, 1, 1, 1, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("Hz", "fn_Hz", 1, 0, 2, 0, 1, 1, 0),
        ("Q", "fn_Q", 1, 0, 2, 0, 1, 1, 0),
        ("ch", "fn_ch", 1, 0, 2, 0, 1, 1, 0),
        ("cm", "fn_cm", 1, 0, 2, 0, 1, 1, 0),
        ("cqb", "fn_cqb", 1, 0, 2, 0, 1, 1, 0),
        ("cqh", "fn_cqh", 1, 0, 2, 0, 1, 1, 0),
        ("cqi", "fn_cqi", 1, 0, 2, 0, 1, 1, 0),
        ("cqmax", "fn_cqmax", 1, 0, 2, 0, 1, 1, 0),
        ("cqmin", "fn_cqmin", 1, 0, 2, 0, 1, 1, 0),
        ("cqw", "fn_cqw", 1, 0, 2, 0, 1, 1, 0),
        ("deg", "fn_deg", 1, 0, 2, 0, 1, 1, 0),
        ("dpcm", "fn_dpcm", 1, 0, 2, 0, 1, 1, 0),
        ("dpi", "fn_dpi", 1, 0, 2, 0, 1, 1, 0),
        ("dppx", "fn_dppx", 1, 0, 2, 0, 1, 1, 0),
        ("dvb", "fn_dvb", 1, 0, 2, 0, 1, 1, 0),
        ("dvh", "fn_dvh", 1, 0, 2, 0, 1, 1, 0),
        ("dvi", "fn_dvi", 1, 0, 2, 0, 1, 1, 0),
        ("dvmax", "fn_dvmax", 1, 0, 2, 0, 1, 1, 0),
        ("dvmin", "fn_dvmin", 1, 0, 2, 0, 1, 1, 0),
        ("dvw", "fn_dvw", 1, 0, 2, 0, 1, 1, 0),
        ("em", "fn_em", 1, 0, 2, 0, 1, 1, 0),
        ("escape", "fn_escape", 1, 0, 2, 0, 1, 1, 0),
        ("ex", "fn_ex", 1, 0, 2, 0, 1, 1, 0),
        ("fr", "fn_fr", 1, 0, 2, 0, 1, 1, 0),
        ("grad", "fn_grad", 1, 0, 2, 0, 1, 1, 0),
        ("in", "fn_in", 1, 0, 2, 0, 1, 1, 0),
        ("kHz", "fn_kHz", 1, 0, 2, 0, 1, 1, 0),
        ("lvb", "fn_lvb", 1, 0, 2, 0, 1, 1, 0),
        ("lvh", "fn_lvh", 1, 0, 2, 0, 1, 1, 0),
        ("lvi", "fn_lvi", 1, 0, 2, 0, 1, 1, 0),
        ("lvmax", "fn_lvmax", 1, 0, 2, 0, 1, 1, 0),
        ("lvmin", "fn_lvmin", 1, 0, 2, 0, 1, 1, 0),
        ("lvw", "fn_lvw", 1, 0, 2, 0, 1, 1, 0),
        ("mm", "fn_mm", 1, 0, 2, 0, 1, 1, 0),
        ("ms", "fn_ms", 1, 0, 2, 0, 1, 1, 0),
        ("number", "fn_number", 1, 0, 2, 0, 1, 1, 0),
        ("pc", "fn_pc", 1, 0, 2, 0, 1, 1, 0),
        ("percent", "fn_percent", 1, 0, 2, 0, 1, 1, 0),
        ("pt", "fn_pt", 1, 0, 2, 0, 1, 1, 0),
        ("px", "fn_px", 1, 0, 2, 0, 1, 1, 0),
        ("rad", "fn_rad", 1, 0, 2, 0, 1, 1, 0),
        ("registerProperty", "fn_registerProperty", 1, 0, 2, 0, 1, 1, 0),
        ("rem", "fn_rem", 1, 0, 2, 0, 1, 1, 0),
        ("s", "fn_s", 1, 0, 2, 0, 1, 1, 0),
        ("supports", "fn_supports", 1, 0, 2, 0, 1, 1, 0),
        ("svb", "fn_svb", 1, 0, 2, 0, 1, 1, 0),
        ("svh", "fn_svh", 1, 0, 2, 0, 1, 1, 0),
        ("svi", "fn_svi", 1, 0, 2, 0, 1, 1, 0),
        ("svmax", "fn_svmax", 1, 0, 2, 0, 1, 1, 0),
        ("svmin", "fn_svmin", 1, 0, 2, 0, 1, 1, 0),
        ("svw", "fn_svw", 1, 0, 2, 0, 1, 1, 0),
        ("turn", "fn_turn", 1, 0, 2, 0, 1, 1, 0),
        ("vb", "fn_vb", 1, 0, 2, 0, 1, 1, 0),
        ("vh", "fn_vh", 1, 0, 2, 0, 1, 1, 0),
        ("vi", "fn_vi", 1, 0, 2, 0, 1, 1, 0),
        ("vmax", "fn_vmax", 1, 0, 2, 0, 1, 1, 0),
        ("vmin", "fn_vmin", 1, 0, 2, 0, 1, 1, 0),
        ("vw", "fn_vw", 1, 0, 2, 0, 1, 1, 0),
        ("cap", "fn_cap", 1, 0, 2, 0, 1, 1, 0),
        ("rcap", "fn_rcap", 1, 0, 2, 0, 1, 1, 0),
        ("ic", "fn_ic", 1, 0, 2, 0, 1, 1, 0),
        ("lh", "fn_lh", 1, 0, 2, 0, 1, 1, 0),
        ("rch", "fn_rch", 1, 0, 2, 0, 1, 1, 0),
        ("rex", "fn_rex", 1, 0, 2, 0, 1, 1, 0),
        ("ric", "fn_ric", 1, 0, 2, 0, 1, 1, 0),
        ("rlh", "fn_rlh", 1, 0, 2, 0, 1, 1, 0),
        ("x", "fn_x", 1, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def get_highlights(cls):
        logger.debug(f'patch -> v8_css.py -> CSS.highlights -> get attr')

    @classmethod
    def get_layoutWorklet(cls):
        logger.debug(f'patch -> v8_css.py -> CSS.layoutWorklet -> get attr')

    @classmethod
    def get_animationWorklet(cls):
        logger.debug(f'patch -> v8_css.py -> CSS.animationWorklet -> get attr')

    @classmethod
    def get_paintWorklet(cls):
        logger.debug(f'patch -> v8_css.py -> CSS.paintWorklet -> get attr')

    @classmethod
    def fn_Hz(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.Hz{tuple(args)} -> method')

    @classmethod
    def fn_Q(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.Q{tuple(args)} -> method')

    @classmethod
    def fn_ch(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.ch{tuple(args)} -> method')

    @classmethod
    def fn_cm(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cm{tuple(args)} -> method')

    @classmethod
    def fn_cqb(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqb{tuple(args)} -> method')

    @classmethod
    def fn_cqh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqh{tuple(args)} -> method')

    @classmethod
    def fn_cqi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqi{tuple(args)} -> method')

    @classmethod
    def fn_cqmax(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqmax{tuple(args)} -> method')

    @classmethod
    def fn_cqmin(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqmin{tuple(args)} -> method')

    @classmethod
    def fn_cqw(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cqw{tuple(args)} -> method')

    @classmethod
    def fn_deg(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.deg{tuple(args)} -> method')

    @classmethod
    def fn_dpcm(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dpcm{tuple(args)} -> method')

    @classmethod
    def fn_dpi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dpi{tuple(args)} -> method')

    @classmethod
    def fn_dppx(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dppx{tuple(args)} -> method')

    @classmethod
    def fn_dvb(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvb{tuple(args)} -> method')

    @classmethod
    def fn_dvh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvh{tuple(args)} -> method')

    @classmethod
    def fn_dvi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvi{tuple(args)} -> method')

    @classmethod
    def fn_dvmax(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvmax{tuple(args)} -> method')

    @classmethod
    def fn_dvmin(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvmin{tuple(args)} -> method')

    @classmethod
    def fn_dvw(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.dvw{tuple(args)} -> method')

    @classmethod
    def fn_em(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.em{tuple(args)} -> method')

    @classmethod
    def fn_escape(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.escape{tuple(args)} -> method')

    @classmethod
    def fn_ex(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.ex{tuple(args)} -> method')

    @classmethod
    def fn_fr(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.fr{tuple(args)} -> method')

    @classmethod
    def fn_grad(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.grad{tuple(args)} -> method')

    @classmethod
    def fn_in(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.in{tuple(args)} -> method')

    @classmethod
    def fn_kHz(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.kHz{tuple(args)} -> method')

    @classmethod
    def fn_lvb(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvb{tuple(args)} -> method')

    @classmethod
    def fn_lvh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvh{tuple(args)} -> method')

    @classmethod
    def fn_lvi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvi{tuple(args)} -> method')

    @classmethod
    def fn_lvmax(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvmax{tuple(args)} -> method')

    @classmethod
    def fn_lvmin(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvmin{tuple(args)} -> method')

    @classmethod
    def fn_lvw(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lvw{tuple(args)} -> method')

    @classmethod
    def fn_mm(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.mm{tuple(args)} -> method')

    @classmethod
    def fn_ms(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.ms{tuple(args)} -> method')

    @classmethod
    def fn_number(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.number{tuple(args)} -> method')

    @classmethod
    def fn_pc(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.pc{tuple(args)} -> method')

    @classmethod
    def fn_percent(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.percent{tuple(args)} -> method')

    @classmethod
    def fn_pt(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.pt{tuple(args)} -> method')

    @classmethod
    def fn_px(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.px{tuple(args)} -> method')

    @classmethod
    def fn_rad(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rad{tuple(args)} -> method')

    @classmethod
    def fn_registerProperty(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.registerProperty{tuple(args)} -> method')

    @classmethod
    def fn_rem(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rem{tuple(args)} -> method')

    @classmethod
    def fn_s(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.s{tuple(args)} -> method')

    @classmethod
    def fn_supports(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.supports{tuple(args)} -> method')

    @classmethod
    def fn_svb(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svb{tuple(args)} -> method')

    @classmethod
    def fn_svh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svh{tuple(args)} -> method')

    @classmethod
    def fn_svi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svi{tuple(args)} -> method')

    @classmethod
    def fn_svmax(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svmax{tuple(args)} -> method')

    @classmethod
    def fn_svmin(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svmin{tuple(args)} -> method')

    @classmethod
    def fn_svw(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.svw{tuple(args)} -> method')

    @classmethod
    def fn_turn(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.turn{tuple(args)} -> method')

    @classmethod
    def fn_vb(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vb{tuple(args)} -> method')

    @classmethod
    def fn_vh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vh{tuple(args)} -> method')

    @classmethod
    def fn_vi(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vi{tuple(args)} -> method')

    @classmethod
    def fn_vmax(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vmax{tuple(args)} -> method')

    @classmethod
    def fn_vmin(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vmin{tuple(args)} -> method')

    @classmethod
    def fn_vw(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.vw{tuple(args)} -> method')

    @classmethod
    def fn_cap(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.cap{tuple(args)} -> method')

    @classmethod
    def fn_rcap(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rcap{tuple(args)} -> method')

    @classmethod
    def fn_ic(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.ic{tuple(args)} -> method')

    @classmethod
    def fn_lh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.lh{tuple(args)} -> method')

    @classmethod
    def fn_rch(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rch{tuple(args)} -> method')

    @classmethod
    def fn_rex(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rex{tuple(args)} -> method')

    @classmethod
    def fn_ric(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.ric{tuple(args)} -> method')

    @classmethod
    def fn_rlh(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.rlh{tuple(args)} -> method')

    @classmethod
    def fn_x(cls, *args):
        logger.debug(f'patch -> v8_css.py -> CSS.x{tuple(args)} -> method')
