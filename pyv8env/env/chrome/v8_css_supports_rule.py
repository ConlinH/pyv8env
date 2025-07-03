from .flags import *
from .v8_css_condition_rule import CSSConditionRule


@construct_100001
class CSSSupportsRule(CSSConditionRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSSupportsRule, self).__init__(*args, **kw)
