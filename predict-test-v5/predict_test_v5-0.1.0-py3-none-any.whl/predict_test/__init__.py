# importing sys
import sys
import os
cdir = os.getcwd()
cdir+="/models/"
# adding src/model/ to the system path
# sys.path.insert(0, '/home/mosfak/Desktop/Predict-the-Collision-and-Save-the-Earth-master/src/models/')
sys.path.insert(0, cdir)
# from src.models.__init__ import *

 
# importing the main
# from __init__ import *
from __init__ import main 

# str = "/home/mosfak/Desktop/Predict-the-Collision-and-Save-the-Earth-master/prediict/data/neo.csv"
# # str = sys.argv[1]
# # print(str)
# # readd(str)
# main(str, 1)
