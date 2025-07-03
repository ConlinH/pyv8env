from .flags import *


@construct_000001
class DigitalGoodsService:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("consume", "fn_consume", 1, 0, 1, 0, 1, 0, 0),
        ("getDetails", "fn_getDetails", 1, 0, 1, 0, 1, 0, 0),
        ("listPurchases", "fn_listPurchases", 0, 0, 1, 0, 1, 0, 0),
        ("listPurchaseHistory", "fn_listPurchaseHistory", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_consume(self, *args):
        logger.debug(f'patch -> v8_digital_goods_service.py -> DigitalGoodsService.consume{tuple(args)} -> method')

    def fn_getDetails(self, *args):
        logger.debug(f'patch -> v8_digital_goods_service.py -> DigitalGoodsService.getDetails{tuple(args)} -> method')

    def fn_listPurchases(self, *args):
        logger.debug(f'patch -> v8_digital_goods_service.py -> DigitalGoodsService.listPurchases{tuple(args)} -> method')

    def fn_listPurchaseHistory(self, *args):
        logger.debug(f'patch -> v8_digital_goods_service.py -> DigitalGoodsService.listPurchaseHistory{tuple(args)} -> method')
