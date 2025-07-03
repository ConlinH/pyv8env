from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class AccessibleNode(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AccessibleNode, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("activeDescendant", "get_activeDescendant", "set_activeDescendant", 0, 1, 0, 0, 0, 0, 1),
        ("atomic", "get_atomic", "set_atomic", 0, 1, 0, 0, 0, 0, 1),
        ("autocomplete", "get_autocomplete", "set_autocomplete", 0, 1, 0, 0, 0, 0, 1),
        ("busy", "get_busy", "set_busy", 0, 1, 0, 0, 0, 0, 1),
        ("checked", "get_checked", "set_checked", 0, 1, 0, 0, 0, 0, 1),
        ("colCount", "get_colCount", "set_colCount", 0, 1, 0, 0, 0, 0, 1),
        ("colIndex", "get_colIndex", "set_colIndex", 0, 1, 0, 0, 0, 0, 1),
        ("colSpan", "get_colSpan", "set_colSpan", 0, 1, 0, 0, 0, 0, 1),
        ("controls", "get_controls", "set_controls", 0, 1, 0, 0, 0, 0, 1),
        ("current", "get_current", "set_current", 0, 1, 0, 0, 0, 0, 1),
        ("describedBy", "get_describedBy", "set_describedBy", 0, 1, 0, 0, 0, 0, 1),
        ("details", "get_details", "set_details", 0, 1, 0, 0, 0, 0, 1),
        ("disabled", "get_disabled", "set_disabled", 0, 1, 0, 0, 0, 0, 1),
        ("errorMessage", "get_errorMessage", "set_errorMessage", 0, 1, 0, 0, 0, 0, 1),
        ("expanded", "get_expanded", "set_expanded", 0, 1, 0, 0, 0, 0, 1),
        ("flowTo", "get_flowTo", "set_flowTo", 0, 1, 0, 0, 0, 0, 1),
        ("hasPopup", "get_hasPopup", "set_hasPopup", 0, 1, 0, 0, 0, 0, 1),
        ("hidden", "get_hidden", "set_hidden", 0, 1, 0, 0, 0, 0, 1),
        ("invalid", "get_invalid", "set_invalid", 0, 1, 0, 0, 0, 0, 1),
        ("keyShortcuts", "get_keyShortcuts", "set_keyShortcuts", 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),
        ("labeledBy", "get_labeledBy", "set_labeledBy", 0, 1, 0, 0, 0, 0, 1),
        ("level", "get_level", "set_level", 0, 1, 0, 0, 0, 0, 1),
        ("live", "get_live", "set_live", 0, 1, 0, 0, 0, 0, 1),
        ("modal", "get_modal", "set_modal", 0, 1, 0, 0, 0, 0, 1),
        ("multiline", "get_multiline", "set_multiline", 0, 1, 0, 0, 0, 0, 1),
        ("multiselectable", "get_multiselectable", "set_multiselectable", 0, 1, 0, 0, 0, 0, 1),
        ("orientation", "get_orientation", "set_orientation", 0, 1, 0, 0, 0, 0, 1),
        ("owns", "get_owns", "set_owns", 0, 1, 0, 0, 0, 0, 1),
        ("placeholder", "get_placeholder", "set_placeholder", 0, 1, 0, 0, 0, 0, 1),
        ("posInSet", "get_posInSet", "set_posInSet", 0, 1, 0, 0, 0, 0, 1),
        ("pressed", "get_pressed", "set_pressed", 0, 1, 0, 0, 0, 0, 1),
        ("readOnly", "get_readOnly", "set_readOnly", 0, 1, 0, 0, 0, 0, 1),
        ("relevant", "get_relevant", "set_relevant", 0, 1, 0, 0, 0, 0, 1),
        ("required", "get_required", "set_required", 0, 1, 0, 0, 0, 0, 1),
        ("role", "get_role", "set_role", 0, 1, 0, 0, 0, 0, 1),
        ("roleDescription", "get_roleDescription", "set_roleDescription", 0, 1, 0, 0, 0, 0, 1),
        ("rowCount", "get_rowCount", "set_rowCount", 0, 1, 0, 0, 0, 0, 1),
        ("rowIndex", "get_rowIndex", "set_rowIndex", 0, 1, 0, 0, 0, 0, 1),
        ("rowSpan", "get_rowSpan", "set_rowSpan", 0, 1, 0, 0, 0, 0, 1),
        ("selected", "get_selected", "set_selected", 0, 1, 0, 0, 0, 0, 1),
        ("setSize", "get_setSize", "set_setSize", 0, 1, 0, 0, 0, 0, 1),
        ("sort", "get_sort", "set_sort", 0, 1, 0, 0, 0, 0, 1),
        ("valueMax", "get_valueMax", "set_valueMax", 0, 1, 0, 0, 0, 0, 1),
        ("valueMin", "get_valueMin", "set_valueMin", 0, 1, 0, 0, 0, 0, 1),
        ("valueNow", "get_valueNow", "set_valueNow", 0, 1, 0, 0, 0, 0, 1),
        ("valueText", "get_valueText", "set_valueText", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessibleclick", "get_onaccessibleclick", "set_onaccessibleclick", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessiblecontextmenu", "get_onaccessiblecontextmenu", "set_onaccessiblecontextmenu", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessibledecrement", "get_onaccessibledecrement", "set_onaccessibledecrement", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessiblefocus", "get_onaccessiblefocus", "set_onaccessiblefocus", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessibleincrement", "get_onaccessibleincrement", "set_onaccessibleincrement", 0, 1, 0, 0, 0, 0, 1),
        ("onaccessiblescrollintoview", "get_onaccessiblescrollintoview", "set_onaccessiblescrollintoview", 0, 1, 0, 0, 0, 0, 1),
        ("childNodes", "get_childNodes", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("appendChild", "fn_appendChild", 1, 0, 1, 0, 0, 0, 0),
        ("removeChild", "fn_removeChild", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_activeDescendant(self):
        val = self._attr.get('activeDescendant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.activeDescendant -> get attr')

    def set_activeDescendant(self, val):
        self._attr['activeDescendant'] = val

    def get_atomic(self):
        val = self._attr.get('atomic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.atomic -> get attr')

    def set_atomic(self, val):
        self._attr['atomic'] = val

    def get_autocomplete(self):
        val = self._attr.get('autocomplete')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.autocomplete -> get attr')

    def set_autocomplete(self, val):
        self._attr['autocomplete'] = val

    def get_busy(self):
        val = self._attr.get('busy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.busy -> get attr')

    def set_busy(self, val):
        self._attr['busy'] = val

    def get_checked(self):
        val = self._attr.get('checked')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.checked -> get attr')

    def set_checked(self, val):
        self._attr['checked'] = val

    def get_colCount(self):
        val = self._attr.get('colCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.colCount -> get attr')

    def set_colCount(self, val):
        self._attr['colCount'] = val

    def get_colIndex(self):
        val = self._attr.get('colIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.colIndex -> get attr')

    def set_colIndex(self, val):
        self._attr['colIndex'] = val

    def get_colSpan(self):
        val = self._attr.get('colSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.colSpan -> get attr')

    def set_colSpan(self, val):
        self._attr['colSpan'] = val

    def get_controls(self):
        val = self._attr.get('controls')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.controls -> get attr')

    def set_controls(self, val):
        self._attr['controls'] = val

    def get_current(self):
        val = self._attr.get('current')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.current -> get attr')

    def set_current(self, val):
        self._attr['current'] = val

    def get_describedBy(self):
        val = self._attr.get('describedBy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.describedBy -> get attr')

    def set_describedBy(self, val):
        self._attr['describedBy'] = val

    def get_details(self):
        val = self._attr.get('details')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.details -> get attr')

    def set_details(self, val):
        self._attr['details'] = val

    def get_disabled(self):
        val = self._attr.get('disabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.disabled -> get attr')

    def set_disabled(self, val):
        self._attr['disabled'] = val

    def get_errorMessage(self):
        val = self._attr.get('errorMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.errorMessage -> get attr')

    def set_errorMessage(self, val):
        self._attr['errorMessage'] = val

    def get_expanded(self):
        val = self._attr.get('expanded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.expanded -> get attr')

    def set_expanded(self, val):
        self._attr['expanded'] = val

    def get_flowTo(self):
        val = self._attr.get('flowTo')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.flowTo -> get attr')

    def set_flowTo(self, val):
        self._attr['flowTo'] = val

    def get_hasPopup(self):
        val = self._attr.get('hasPopup')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.hasPopup -> get attr')

    def set_hasPopup(self, val):
        self._attr['hasPopup'] = val

    def get_hidden(self):
        val = self._attr.get('hidden')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.hidden -> get attr')

    def set_hidden(self, val):
        self._attr['hidden'] = val

    def get_invalid(self):
        val = self._attr.get('invalid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.invalid -> get attr')

    def set_invalid(self, val):
        self._attr['invalid'] = val

    def get_keyShortcuts(self):
        val = self._attr.get('keyShortcuts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.keyShortcuts -> get attr')

    def set_keyShortcuts(self, val):
        self._attr['keyShortcuts'] = val

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def get_labeledBy(self):
        val = self._attr.get('labeledBy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.labeledBy -> get attr')

    def set_labeledBy(self, val):
        self._attr['labeledBy'] = val

    def get_level(self):
        val = self._attr.get('level')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.level -> get attr')

    def set_level(self, val):
        self._attr['level'] = val

    def get_live(self):
        val = self._attr.get('live')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.live -> get attr')

    def set_live(self, val):
        self._attr['live'] = val

    def get_modal(self):
        val = self._attr.get('modal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.modal -> get attr')

    def set_modal(self, val):
        self._attr['modal'] = val

    def get_multiline(self):
        val = self._attr.get('multiline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.multiline -> get attr')

    def set_multiline(self, val):
        self._attr['multiline'] = val

    def get_multiselectable(self):
        val = self._attr.get('multiselectable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.multiselectable -> get attr')

    def set_multiselectable(self, val):
        self._attr['multiselectable'] = val

    def get_orientation(self):
        val = self._attr.get('orientation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.orientation -> get attr')

    def set_orientation(self, val):
        self._attr['orientation'] = val

    def get_owns(self):
        val = self._attr.get('owns')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.owns -> get attr')

    def set_owns(self, val):
        self._attr['owns'] = val

    def get_placeholder(self):
        val = self._attr.get('placeholder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.placeholder -> get attr')

    def set_placeholder(self, val):
        self._attr['placeholder'] = val

    def get_posInSet(self):
        val = self._attr.get('posInSet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.posInSet -> get attr')

    def set_posInSet(self, val):
        self._attr['posInSet'] = val

    def get_pressed(self):
        val = self._attr.get('pressed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.pressed -> get attr')

    def set_pressed(self, val):
        self._attr['pressed'] = val

    def get_readOnly(self):
        val = self._attr.get('readOnly')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.readOnly -> get attr')

    def set_readOnly(self, val):
        self._attr['readOnly'] = val

    def get_relevant(self):
        val = self._attr.get('relevant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.relevant -> get attr')

    def set_relevant(self, val):
        self._attr['relevant'] = val

    def get_required(self):
        val = self._attr.get('required')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.required -> get attr')

    def set_required(self, val):
        self._attr['required'] = val

    def get_role(self):
        val = self._attr.get('role')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.role -> get attr')

    def set_role(self, val):
        self._attr['role'] = val

    def get_roleDescription(self):
        val = self._attr.get('roleDescription')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.roleDescription -> get attr')

    def set_roleDescription(self, val):
        self._attr['roleDescription'] = val

    def get_rowCount(self):
        val = self._attr.get('rowCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.rowCount -> get attr')

    def set_rowCount(self, val):
        self._attr['rowCount'] = val

    def get_rowIndex(self):
        val = self._attr.get('rowIndex')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.rowIndex -> get attr')

    def set_rowIndex(self, val):
        self._attr['rowIndex'] = val

    def get_rowSpan(self):
        val = self._attr.get('rowSpan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.rowSpan -> get attr')

    def set_rowSpan(self, val):
        self._attr['rowSpan'] = val

    def get_selected(self):
        val = self._attr.get('selected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.selected -> get attr')

    def set_selected(self, val):
        self._attr['selected'] = val

    def get_setSize(self):
        val = self._attr.get('setSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.setSize -> get attr')

    def set_setSize(self, val):
        self._attr['setSize'] = val

    def get_sort(self):
        val = self._attr.get('sort')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.sort -> get attr')

    def set_sort(self, val):
        self._attr['sort'] = val

    def get_valueMax(self):
        val = self._attr.get('valueMax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.valueMax -> get attr')

    def set_valueMax(self, val):
        self._attr['valueMax'] = val

    def get_valueMin(self):
        val = self._attr.get('valueMin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.valueMin -> get attr')

    def set_valueMin(self, val):
        self._attr['valueMin'] = val

    def get_valueNow(self):
        val = self._attr.get('valueNow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.valueNow -> get attr')

    def set_valueNow(self, val):
        self._attr['valueNow'] = val

    def get_valueText(self):
        val = self._attr.get('valueText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.valueText -> get attr')

    def set_valueText(self, val):
        self._attr['valueText'] = val

    def get_onaccessibleclick(self):
        val = self._attr.get('onaccessibleclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessibleclick -> get attr')

    def set_onaccessibleclick(self, val):
        self._attr['onaccessibleclick'] = val

    def get_onaccessiblecontextmenu(self):
        val = self._attr.get('onaccessiblecontextmenu')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessiblecontextmenu -> get attr')

    def set_onaccessiblecontextmenu(self, val):
        self._attr['onaccessiblecontextmenu'] = val

    def get_onaccessibledecrement(self):
        val = self._attr.get('onaccessibledecrement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessibledecrement -> get attr')

    def set_onaccessibledecrement(self, val):
        self._attr['onaccessibledecrement'] = val

    def get_onaccessiblefocus(self):
        val = self._attr.get('onaccessiblefocus')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessiblefocus -> get attr')

    def set_onaccessiblefocus(self, val):
        self._attr['onaccessiblefocus'] = val

    def get_onaccessibleincrement(self):
        val = self._attr.get('onaccessibleincrement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessibleincrement -> get attr')

    def set_onaccessibleincrement(self, val):
        self._attr['onaccessibleincrement'] = val

    def get_onaccessiblescrollintoview(self):
        val = self._attr.get('onaccessiblescrollintoview')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.onaccessiblescrollintoview -> get attr')

    def set_onaccessiblescrollintoview(self, val):
        self._attr['onaccessiblescrollintoview'] = val

    def get_childNodes(self):
        val = self._attr.get('childNodes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.childNodes -> get attr')

    def fn_appendChild(self, *args):
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.appendChild{tuple(args)} -> method')

    def fn_removeChild(self, *args):
        logger.debug(f'patch -> v8_accessible_node.py -> AccessibleNode.removeChild{tuple(args)} -> method')
