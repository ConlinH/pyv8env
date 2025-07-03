from .flags import *


@construct_000001
class SequenceTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getElementSequence", "fn_getElementSequence", 0, 0, 1, 0, 0, 0, 0),
        ("identityByteStringSequenceSequence", "fn_identityByteStringSequenceSequence", 1, 0, 1, 0, 0, 0, 0),
        ("identityDoubleSequence", "fn_identityDoubleSequence", 1, 0, 1, 0, 0, 0, 0),
        ("identityFoodEnumSequence", "fn_identityFoodEnumSequence", 1, 0, 1, 0, 0, 0, 0),
        ("identityLongSequence", "fn_identityLongSequence", 1, 0, 1, 0, 0, 0, 0),
        ("identityOctetSequenceOrNull", "fn_identityOctetSequenceOrNull", 1, 0, 1, 0, 0, 0, 0),
        ("setElementSequence", "fn_setElementSequence", 1, 0, 1, 0, 0, 0, 0),
        ("unionReceivedSequence", "fn_unionReceivedSequence", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_getElementSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.getElementSequence{tuple(args)} -> method')

    def fn_identityByteStringSequenceSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.identityByteStringSequenceSequence{tuple(args)} -> method')

    def fn_identityDoubleSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.identityDoubleSequence{tuple(args)} -> method')

    def fn_identityFoodEnumSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.identityFoodEnumSequence{tuple(args)} -> method')

    def fn_identityLongSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.identityLongSequence{tuple(args)} -> method')

    def fn_identityOctetSequenceOrNull(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.identityOctetSequenceOrNull{tuple(args)} -> method')

    def fn_setElementSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.setElementSequence{tuple(args)} -> method')

    def fn_unionReceivedSequence(self, *args):
        logger.debug(f'patch -> v8_sequence_test.py -> SequenceTest.unionReceivedSequence{tuple(args)} -> method')
