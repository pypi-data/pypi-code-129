"""_2551.py

ActiveFESubstructureSelectionGroup
"""


from mastapy.system_model.part_model.configurations import _2556, _2550
from mastapy.system_model.part_model import _2393
from mastapy.system_model.fe import _2322
from mastapy._internal.python_net import python_net_import

_ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveFESubstructureSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveFESubstructureSelectionGroup',)


class ActiveFESubstructureSelectionGroup(_2556.PartDetailConfiguration['_2550.ActiveFESubstructureSelection', '_2393.FEPart', '_2322.FESubstructure']):
    """ActiveFESubstructureSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_FE_SUBSTRUCTURE_SELECTION_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ActiveFESubstructureSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
