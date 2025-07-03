from .flags import *


@construct_100001
class ValidityState:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("valueMissing", "get_valueMissing", None, 0, 1, 0, 0, 0, 0, 1),
        ("typeMismatch", "get_typeMismatch", None, 0, 1, 0, 0, 0, 0, 1),
        ("patternMismatch", "get_patternMismatch", None, 0, 1, 0, 0, 0, 0, 1),
        ("tooLong", "get_tooLong", None, 0, 1, 0, 0, 0, 0, 1),
        ("tooShort", "get_tooShort", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeUnderflow", "get_rangeUnderflow", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeOverflow", "get_rangeOverflow", None, 0, 1, 0, 0, 0, 0, 1),
        ("stepMismatch", "get_stepMismatch", None, 0, 1, 0, 0, 0, 0, 1),
        ("badInput", "get_badInput", None, 0, 1, 0, 0, 0, 0, 1),
        ("customError", "get_customError", None, 0, 1, 0, 0, 0, 0, 1),
        ("valid", "get_valid", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_valueMissing(self):
        val = self._attr.get('valueMissing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.valueMissing -> get attr')

    def get_typeMismatch(self):
        val = self._attr.get('typeMismatch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.typeMismatch -> get attr')

    def get_patternMismatch(self):
        val = self._attr.get('patternMismatch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.patternMismatch -> get attr')

    def get_tooLong(self):
        val = self._attr.get('tooLong')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.tooLong -> get attr')

    def get_tooShort(self):
        val = self._attr.get('tooShort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.tooShort -> get attr')

    def get_rangeUnderflow(self):
        val = self._attr.get('rangeUnderflow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.rangeUnderflow -> get attr')

    def get_rangeOverflow(self):
        val = self._attr.get('rangeOverflow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.rangeOverflow -> get attr')

    def get_stepMismatch(self):
        val = self._attr.get('stepMismatch')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.stepMismatch -> get attr')

    def get_badInput(self):
        val = self._attr.get('badInput')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.badInput -> get attr')

    def get_customError(self):
        val = self._attr.get('customError')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.customError -> get attr')

    def get_valid(self):
        val = self._attr.get('valid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_validity_state.py -> ValidityState.valid -> get attr')
