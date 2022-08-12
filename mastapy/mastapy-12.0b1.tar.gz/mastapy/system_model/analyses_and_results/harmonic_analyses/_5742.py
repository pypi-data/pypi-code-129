"""_5742.py

StraightBevelPlanetGearHarmonicAnalysis
"""


from mastapy.system_model.part_model.gears import _2488
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2753
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5736
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'StraightBevelPlanetGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearHarmonicAnalysis',)


class StraightBevelPlanetGearHarmonicAnalysis(_5736.StraightBevelDiffGearHarmonicAnalysis):
    """StraightBevelPlanetGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2753.StraightBevelPlanetGearSystemDeflection':
        """StraightBevelPlanetGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
