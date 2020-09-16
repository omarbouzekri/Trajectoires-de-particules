import numpy as np
import cv2
from Commun import morpho, strel
from trait import count_objects
import sys
sys.setrecursionlimit(10 ** 6)


imag = cv2.imread('une_trajectoire_angle_50.png', cv2.IMREAD_GRAYSCALE)



for angle in range(0, 100,10):
# On construit la ligne
    el = strel.build("ligne", 20, angle)
# On effectue la fermeture
    fe = morpho.myclose(imag, el)
# On compte le nombre de composantes 8 connexes
    con = count_objects(fe)
    print(angle,con)

