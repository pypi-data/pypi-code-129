import number_guessing,sys,os
from setuptools import setup

try:os.chdir(os.path.split(__file__)[0])
except:pass

setup(
  name='number-guessing',
  version=number_guessing.__version__,
  description=number_guessing.__doc__.replace('\n',''),
  long_description="HAVE FUN!",
  author=number_guessing.__author__,
  author_email=number_guessing.__email__,
  url="https://github.com/qfcy/Python/blob/main/GuessingNumber.py",
  py_modules=['number_guessing'], #这里是代码所在的文件名称
  keywords=["number","guess","game","tkinter"],
  classifiers=[
      'Programming Language :: Python',
      "Natural Language :: Chinese (Simplified)",
      "Topic :: Games/Entertainment :: Puzzle Games"],
)

if "install" in sys.argv:
    os.system("pythonw -m number_guessing")
