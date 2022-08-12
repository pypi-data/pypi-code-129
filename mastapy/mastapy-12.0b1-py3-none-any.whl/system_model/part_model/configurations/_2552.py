"""_2552.py

ActiveShaftDesignSelection
"""


from mastapy.system_model.part_model.configurations import _2557
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.shafts import _43
from mastapy._internal.python_net import python_net_import

_ACTIVE_SHAFT_DESIGN_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'ActiveShaftDesignSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveShaftDesignSelection',)


class ActiveShaftDesignSelection(_2557.PartDetailSelection['_2422.Shaft', '_43.SimpleShaftDefinition']):
    """ActiveShaftDesignSelection

    This is a mastapy class.
    """

    TYPE = _ACTIVE_SHAFT_DESIGN_SELECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ActiveShaftDesignSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()
