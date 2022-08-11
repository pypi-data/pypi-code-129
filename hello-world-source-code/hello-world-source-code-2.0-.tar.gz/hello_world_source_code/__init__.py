"This is the source code for Warren Sande's Python book, named Hello World Second Edition."
import os

__version__ = "2.0"
bookname = "Hello World Second Edition"
# import the python files in the package contents
for filename in os.listdir(os.path.split(__file__)[0]):
    if filename.endswith('.py'):
        modname=os.path.split(filename)[1] [:-3]
        try:
            exec("import hello_world_source_code.{0} as {0}"\
                 .format(modname))
        except:pass

del filename, modname
