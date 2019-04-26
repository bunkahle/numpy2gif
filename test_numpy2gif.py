from __future__ import print_function
from numpy2gif import write_gif
import cv2
images = [cv2.cvtColor(cv2.imread("Images/number"+str(i)+".bmp"), cv2.COLOR_BGR2RGB) for i in range(1, 5)]
print(type(images[0]))
print(images[0].shape, images[0].dtype)
write_gif(images, "countdown.gif", fps=3)
write_gif(images[0], "one.gif")