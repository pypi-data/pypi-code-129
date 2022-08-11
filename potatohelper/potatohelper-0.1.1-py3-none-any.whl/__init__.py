import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package],
#    stdout=subprocess.STDOUT,
    stderr=subprocess.DEVNULL)
try:
    install('msvc-runtime')
except Exception as e:
#    print("Don't Worry!!")
    pass
from potatohelper import HandTrackingModule
from potatohelper import FingerCounter
from potatohelper import FaceDetection
from potatohelper import FaceMesh
		
