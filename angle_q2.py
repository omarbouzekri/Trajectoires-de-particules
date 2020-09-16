import cv2
import numpy as np
from Commun import morpho, strel
import sys
sys.setrecursionlimit(10 ** 6)


def max_comp_objet(objects_members, start_point):
    # la première coordonnées de la composante dont la valeur est 255
    x, y = start_point
    # Composante 8 connexes :
    connex = [(x - 1, y), (x, y - 1),
              (x + 1, y), (x, y + 1),
              (x - 1, y + 1), (x - 1, y - 1),
              (x + 1, y + 1), (x + 1, y - 1)]
    A = []
    for point in connex:
        # on rajoute le point dans la liste A
        A.append(point)
        try:
            # On enlève le point  de l'objet
            objects_members.remove(point)
            objects_members.remove((800,554))
            # On exerce la fonction avec les nouveaux paramètres
            max_comp_objet(objects_members, point)
        except ValueError:
            pass
        # le maximum des composantes des différentes listes
        B = max(A)
    return B


def taille_objet(image):
    # la taille de l'image
    width, height = len(image[0]), len(image)
    # On parcoure l'image et on retourne les coordonnées des pixels blanc
    objects_members = [(x, y) for x in range(width) for y in range(height) if image[y][x] == 255]
    n = []
    while objects_members != []:
        o = max_comp_objet(objects_members, objects_members.pop(0))

        # On rajoute ce maximum dans une liste
        n.append(o)
    # On calcule le maximum des différentes listes qu'on a rajouté dans n
    m = max(n)
    # On retourne la taille
    return m,m[0] * m[1]

imag = cv2.imread('quatre_trajectoires_angle_30_50_130_160.png', cv2.IMREAD_GRAYSCALE)

h1 = []
h = np.zeros(10)
i = 0
for angle in range(0, 100, 10):
    # On construit la ligne
    el = strel.build("ligne", 20, angle)
    # On effectue la fermeture
    fe = morpho.myclose(imag, el)
    # On calcule la taille
    m,e = taille_objet(fe)
    h[i] += e
    h1.append(m)
    i+=1

q = np.where(h == max(h))
for s in q:
    print("l'angle est:", s * 10)