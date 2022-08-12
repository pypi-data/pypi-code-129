"""_4314.py

ParametricStudyDOEResultVariable
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility.optimisation import _1514, _1512
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_DOE_RESULT_VARIABLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ParametricStudyDOEResultVariable')


__docformat__ = 'restructuredtext en'
__all__ = ('ParametricStudyDOEResultVariable',)


class ParametricStudyDOEResultVariable(_1512.ParetoOptimisationVariableBase):
    """ParametricStudyDOEResultVariable

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_DOE_RESULT_VARIABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ParametricStudyDOEResultVariable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def entity_name(self) -> 'str':
        """str: 'EntityName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EntityName
        return temp

    @property
    def parameter_name(self) -> 'str':
        """str: 'ParameterName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParameterName
        return temp

    @property
    def target(self) -> '_1514.PropertyTargetForDominantCandidateSearch':
        """PropertyTargetForDominantCandidateSearch: 'Target' is the original name of this property."""

        temp = self.wrapped.Target
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1514.PropertyTargetForDominantCandidateSearch)(value) if value is not None else None

    @target.setter
    def target(self, value: '_1514.PropertyTargetForDominantCandidateSearch'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Target = value
