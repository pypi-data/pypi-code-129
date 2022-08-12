"""_7237.py

CylindricalPlanetGearAdvancedSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2466
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7233
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CylindricalPlanetGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearAdvancedSystemDeflection',)


class CylindricalPlanetGearAdvancedSystemDeflection(_7233.CylindricalGearAdvancedSystemDeflection):
    """CylindricalPlanetGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearAdvancedSystemDeflection.TYPE'):
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
