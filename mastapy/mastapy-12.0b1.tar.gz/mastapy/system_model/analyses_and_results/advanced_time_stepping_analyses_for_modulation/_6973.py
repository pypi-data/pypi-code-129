"""_6973.py

CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.part_model.gears import _2466
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2684
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6970
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation',)


class CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation(_6970.CylindricalGearAdvancedTimeSteppingAnalysisForModulation):
    """CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2466.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
