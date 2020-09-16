import numpy as np
import cv2
from Commun import morpho, strel

from trait import count_objects
import sys

sys.setrecursionlimit(10 ** 6)

def angle_traj(image):
    for angle in range(0, 100, 10):
        el = strel.build("ligne", 20, angle)
        fe = morpho.myclose(image, el)
        con = count_objects(fe)
        if con == 1:
            print("l'angle est:", angle)

imag = cv2.imread('une_trajectoire_angle_30.png', cv2.IMREAD_GRAYSCALE)

print(angle_traj(imag))