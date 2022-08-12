"""_4267.py

CVTParametricStudyTool
"""


from mastapy.system_model.part_model.couplings import _2525
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4236
from mastapy._internal.python_net import python_net_import

_CVT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CVTParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTParametricStudyTool',)


class CVTParametricStudyTool(_4236.BeltDriveParametricStudyTool):
    """CVTParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CVT_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2525.CVT':
        """CVT: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None
