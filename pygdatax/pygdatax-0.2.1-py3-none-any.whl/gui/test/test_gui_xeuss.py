from silx.gui.utils.testutils import TestCaseQt
from .. import gui_xeuss as gx
import weakref
import pytest


# @pytest.mark.usefixtures("TestCaseQt.qapp")
class TestGuiXeuss(TestCaseQt):
    """Test for Viewer class"""

    def testConstruct(self):
        widget = gx.XeussMainWindow()
        self.qWaitForWindowExposed(widget)

    def testDestroy(self):
        widget = gx.XeussMainWindow()
        ref = weakref.ref(widget)
        widget = None
        self.qWaitForDestroy(ref)
    def testDirectory(self):
        widget = gx.XeussMainWindow()
        widget.fileSurvey.set_directory('/')

