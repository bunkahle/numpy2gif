from __future__ import print_function
from gif2numpy import convert
from numpy2gif import write_gif
import cv2

image = "Images/Rotating_earth.gif"
frames, exts, image_specs = convert(image, BGR2RGB=False)
print("len(frames), len(exts), exts[0]['delay_time']", len(frames), len(exts), exts[0]['delay_time'])
write_gif(frames, 'Rotating_earth_new.gif', fps=12)
write_gif(frames[0], 'earth.gif')