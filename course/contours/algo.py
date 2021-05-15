from __future__ import print_function
import cv2 as cv
import argparse 
max_lowThreshold = 100
ratio = 3
kernel_size = 3
val=0
def Canny(image):
    src = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    detected_edges = None
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    detected_edges =  cv.Canny(src_gray,100,200)
    return detected_edges