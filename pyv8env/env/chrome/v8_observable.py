from .flags import *


@construct_111001
class Observable:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("drop", "fn_drop", 1, 0, 1, 0, 0, 0, 0),
        ("every", "fn_every", 1, 0, 1, 0, 1, 0, 0),
        ("filter", "fn_filter", 1, 0, 1, 0, 0, 0, 0),
        ("find", "fn_find", 1, 0, 1, 0, 1, 0, 0),
        ("first", "fn_first", 0, 0, 1, 0, 1, 0, 0),
        ("flatMap", "fn_flatMap", 1, 0, 1, 0, 0, 0, 0),
        ("forEach", "fn_forEach", 1, 0, 1, 0, 1, 0, 0),
        ("inspect", "fn_inspect", 0, 0, 1, 0, 0, 0, 0),
        ("last", "fn_last", 0, 0, 1, 0, 1, 0, 0),
        ("map", "fn_map", 1, 0, 1, 0, 0, 0, 0),
        ("some", "fn_some", 1, 0, 1, 0, 1, 0, 0),
        ("subscribe", "fn_subscribe", 0, 0, 1, 0, 0, 0, 0),
        ("switchMap", "fn_switchMap", 1, 0, 1, 0, 0, 0, 0),
        ("take", "fn_take", 1, 0, 1, 0, 0, 0, 0),
        ("takeUntil", "fn_takeUntil", 1, 0, 1, 0, 0, 0, 0),
        ("toArray", "fn_toArray", 0, 0, 1, 0, 1, 0, 0),
        ("from", "fn_from", 1, 0, 2, 0, 1, 1, 0),

    )

    def fn_drop(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.drop{tuple(args)} -> method')

    def fn_every(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.every{tuple(args)} -> method')

    def fn_filter(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.filter{tuple(args)} -> method')

    def fn_find(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.find{tuple(args)} -> method')

    def fn_first(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.first{tuple(args)} -> method')

    def fn_flatMap(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.flatMap{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.forEach{tuple(args)} -> method')

    def fn_inspect(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.inspect{tuple(args)} -> method')

    def fn_last(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.last{tuple(args)} -> method')

    def fn_map(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.map{tuple(args)} -> method')

    def fn_some(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.some{tuple(args)} -> method')

    def fn_subscribe(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.subscribe{tuple(args)} -> method')

    def fn_switchMap(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.switchMap{tuple(args)} -> method')

    def fn_take(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.take{tuple(args)} -> method')

    def fn_takeUntil(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.takeUntil{tuple(args)} -> method')

    def fn_toArray(self, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.toArray{tuple(args)} -> method')

    @classmethod
    def fn_from(cls, *args):
        logger.debug(f'patch -> v8_observable.py -> Observable.from{tuple(args)} -> method')
