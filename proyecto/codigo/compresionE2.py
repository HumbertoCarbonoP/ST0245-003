import numpy as np
import cv2
import matplotlib.pyplot as plt

def comprimir():
    image = cv2.imread("Proyecto/vaca5.jpg") # Aquí va la ruta del archivo a comprimir con nombre y extensión.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    new_image = []

    for i in range(0, len(image)-1, 2):
        new_row = []
        for j in range(0, len(image[0])-1, 2):
            new_row.append(image[i][j])
        new_image.append(new_row)

    new_imageNP = np.array(new_image)

    cv2.imwrite('comprimido_vaca.jpg', new_imageNP)

def main():
    comprimir()
    print('-'*44, 'La imagen fue comprimida exitosamente', '-'*44)
main()