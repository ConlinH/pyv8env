from .flags import *


@construct_100001
class ComputedAccessibleNode:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("atomic", "get_atomic", None, 0, 1, 0, 0, 0, 0, 1),
        ("busy", "get_busy", None, 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("expanded", "get_expanded", None, 0, 1, 0, 0, 0, 0, 1),
        ("modal", "get_modal", None, 0, 1, 0, 0, 0, 0, 1),
        ("multiline", "get_multiline", None, 0, 1, 0, 0, 0, 0, 1),
        ("multiselectable", "get_multiselectable", None, 0, 1, 0, 0, 0, 0, 1),
        ("readOnly", "get_readOnly", None, 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", None, 0, 1, 0, 0, 0, 0, 1),
        ("selected", "get_selected", None, 0, 1, 0, 0, 0, 0, 1),
        ("colCount", "get_colCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("colIndex", "get_colIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("colSpan", "get_colSpan", None, 0, 1, 0, 0, 0, 0, 1),
        ("level", "get_level", None, 0, 1, 0, 0, 0, 0, 1),
        ("posInSet", "get_posInSet", None, 0, 1, 0, 0, 0, 0, 1),
        ("rowCount", "get_rowCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("rowIndex", "get_rowIndex", None, 0, 1, 0, 0, 0, 0, 1),
        ("rowSpan", "get_rowSpan", None, 0, 1, 0, 0, 0, 0, 1),
        ("setSize", "get_setSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("valueMax", "get_valueMax", None, 0, 1, 0, 0, 0, 0, 1),
        ("valueMin", "get_valueMin", None, 0, 1, 0, 0, 0, 0, 1),
        ("valueNow", "get_valueNow", None, 0, 1, 0, 0, 0, 0, 1),
        ("autocomplete", "get_autocomplete", None, 0, 1, 0, 0, 0, 0, 1),
        ("checked", "get_checked", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyShortcuts", "get_keyShortcuts", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("placeholder", "get_placeholder", None, 0, 1, 0, 0, 0, 0, 1),
        ("role", "get_role", None, 0, 1, 0, 0, 0, 0, 1),
        ("roleDescription", "get_roleDescription", None, 0, 1, 0, 0, 0, 0, 1),
        ("valueText", "get_valueText", None, 0, 1, 0, 0, 0, 0, 1),
        ("parent", "get_parent", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstChild", "get_firstChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastChild", "get_lastChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousSibling", "get_previousSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextSibling", "get_nextSibling", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("ensureUpToDate", "fn_ensureUpToDate", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_atomic(self):
        val = self._attr.get('atomic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.atomic -> get attr')

    def get_busy(self):
        val = self._attr.get('busy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.busy -> get attr')

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.disabled -> get attr')

    def get_expanded(self):
        val = self._attr.get('expanded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.expanded -> get attr')

    def get_modal(self):
        val = self._attr.get('modal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.modal -> get attr')

    def get_multiline(self):
        val = self._attr.get('multiline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.multiline -> get attr')

    def get_multiselectable(self):
        val = self._attr.get('multiselectable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.multiselectable -> get attr')

    def get_readOnly(self):
        val = self._attr.get('readOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.readOnly -> get attr')

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.required -> get attr')

    def get_selected(self):
        val = self._attr.get('selected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.selected -> get attr')

    def get_colCount(self):
        val = self._attr.get('colCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.colCount -> get attr')

    def get_colIndex(self):
        val = self._attr.get('colIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.colIndex -> get attr')

    def get_colSpan(self):
        val = self._attr.get('colSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.colSpan -> get attr')

    def get_level(self):
        val = self._attr.get('level')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.level -> get attr')

    def get_posInSet(self):
        val = self._attr.get('posInSet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.posInSet -> get attr')

    def get_rowCount(self):
        val = self._attr.get('rowCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.rowCount -> get attr')

    def get_rowIndex(self):
        val = self._attr.get('rowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.rowIndex -> get attr')

    def get_rowSpan(self):
        val = self._attr.get('rowSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.rowSpan -> get attr')

    def get_setSize(self):
        val = self._attr.get('setSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.setSize -> get attr')

    def get_valueMax(self):
        val = self._attr.get('valueMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.valueMax -> get attr')

    def get_valueMin(self):
        val = self._attr.get('valueMin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.valueMin -> get attr')

    def get_valueNow(self):
        val = self._attr.get('valueNow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.valueNow -> get attr')

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.autocomplete -> get attr')

    def get_checked(self):
        val = self._attr.get('checked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.checked -> get attr')

    def get_keyShortcuts(self):
        val = self._attr.get('keyShortcuts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.keyShortcuts -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.name -> get attr')

    def get_placeholder(self):
        val = self._attr.get('placeholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.placeholder -> get attr')

    def get_role(self):
        val = self._attr.get('role')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.role -> get attr')

    def get_roleDescription(self):
        val = self._attr.get('roleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.roleDescription -> get attr')

    def get_valueText(self):
        val = self._attr.get('valueText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.valueText -> get attr')

    def get_parent(self):
        val = self._attr.get('parent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.parent -> get attr')

    def get_firstChild(self):
        val = self._attr.get('firstChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.firstChild -> get attr')

    def get_lastChild(self):
        val = self._attr.get('lastChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.lastChild -> get attr')

    def get_previousSibling(self):
        val = self._attr.get('previousSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.previousSibling -> get attr')

    def get_nextSibling(self):
        val = self._attr.get('nextSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.nextSibling -> get attr')

    def fn_ensureUpToDate(self, *args):
        logger.debug(f'patch -> v8_computed_accessible_node.py -> ComputedAccessibleNode.ensureUpToDate{tuple(args)} -> method')
