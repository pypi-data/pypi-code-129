import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('msvc-runtime')

from potatohelper import HandTrackingModule
from potatohelper import FingerCounter
from potatohelper import FaceDetection
from potatohelper import FaceMesh
		
