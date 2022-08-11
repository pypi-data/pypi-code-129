import os

#open the package contents
if __name__=="__main__" and os.name == 'nt':
    os.system('explorer %s' % os.path.split(__file__)[0])
