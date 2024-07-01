import cv2
import numpy as np
from matplotlib import pyplot as plt

image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

if image1.shape != image2.shape:
    print("Les images doivent avoir la même taille et les mêmes dimensions.")
    exit()


gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# soustraction
diff_image = cv2.absdiff(gray_image1, gray_image2)

# seuil de la mise en évidence des diff
_, thresh_image = cv2.threshold(diff_image, 30, 255, cv2.THRESH_BINARY)

# display les images
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1), plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)), plt.title('Image 1')
plt.subplot(2, 2, 2), plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)), plt.title('Image 2')
plt.subplot(2, 2, 3), plt.imshow(diff_image, cmap='gray'), plt.title('Différence')
plt.subplot(2, 2, 4), plt.imshow(thresh_image, cmap='gray'), plt.title('Différences Seuil')
plt.show()
