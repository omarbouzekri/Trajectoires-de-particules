import cv2
import numpy as np

def remove_object(objects_members, start_point):
# la première coordonnées de la composante dont la valeur est 255
    x, y = start_point
# On regarde si la composante est 8 connexes :
    connex = [(x - 1, y), (x, y - 1),
              (x + 1, y), (x, y + 1),
              (x - 1, y+1), (x-1, y-1),
              (x + 1, y+1), (x+1, y-1)]
    for point in connex:
        try:
# On enlève le point  de l'objet
            objects_members.remove(point)
# On exerce la fonction avec les nouveaux paramètres
            remove_object(objects_members, point)
        except ValueError:
            pass

def count_objects(image):
# taille de l'image
    width, height = len(image[0]), len(image)
# On parcoure l'image et on retourne les coordonnées des pixels blanc
    objects_members = [(x, y) for x in range(width) for y in range(height) if image[y][x] == 255]
    objects_count = 0
    while objects_members != []:
        remove_object(objects_members, objects_members.pop(0))
        objects_count += 1
    return objects_count


imag = cv2.imread('une_trajectoire_angle_50.png', cv2.IMREAD_GRAYSCALE)

print(count_objects(imag))
