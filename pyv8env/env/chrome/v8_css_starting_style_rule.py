from .flags import *
from .v8_css_grouping_rule import CSSGroupingRule


@construct_100001
class CSSStartingStyleRule(CSSGroupingRule):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSStartingStyleRule, self).__init__(*args, **kw)
