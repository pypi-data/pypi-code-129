# importing sys
import sys
import os
cdir = os.getcwd()
cdir+="/models/"
# adding src/model/ to the system path
# sys.path.insert(0, '/home/mosfak/Desktop/Predict-the-Collision-and-Save-the-Earth-master/src/models/')
# print(cdir)
sys.path.insert(0, cdir)
# from src.models.__init__ import *

 
# importing the main
# from __init__ import *
from models.__init__ import main_func

# str = "/home/mosfak/Desktop/Predict-the-Collision-and-Save-the-Earth-master/predict_test_02/data/neo.csv"
# # str = sys.argv[1]
# # print(str)
# # readd(str)
# main_func(str, 1)
