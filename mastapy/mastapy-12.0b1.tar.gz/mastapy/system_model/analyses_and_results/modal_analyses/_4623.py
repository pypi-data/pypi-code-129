"""_4623.py

StraightBevelSunGearModalAnalysis
"""


from mastapy.system_model.part_model.gears import _2489
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2754
from mastapy.system_model.analyses_and_results.modal_analyses import _4617
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'StraightBevelSunGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearModalAnalysis',)


class StraightBevelSunGearModalAnalysis(_4617.StraightBevelDiffGearModalAnalysis):
    """StraightBevelSunGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2754.StraightBevelSunGearSystemDeflection':
        """StraightBevelSunGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
