# numpy2gif
Python library to convert single and multiple numpy images to a gif image without PIL or pillow. OpenCV does not support gif images. This a fork of array2gif from Tanya Schlusser found at:
https://github.com/tanyaschlusser/array2gif

Install it with 

    setup.py install
    
or with

    pip install numpy2gif
    
# Usage

You can use the library this way:

    from __future__ import print_function
    from numpy2gif import write_gif
    import cv2
    images = [cv2.cvtColor(cv2.imread("Images/number"+str(i)+".bmp"), cv2.COLOR_BGR2RGB) for i in range(1, 5)]
    print(type(images[0]))
    print(images[0].shape, images[0].dtype)
    write_gif(images, "countdown.gif", fps=3)
    write_gif(images[0], "one.gif")

Try a backward test from converting a gif to numpy frames with the external module gif2numpy and back to a multiple gif image with numpy2gif:

    from __future__ import print_function
    from gif2numpy import convert
    from numpy2gif import write_gif
    import cv2

    image = "Images/Rotating_earth.gif"
    frames, exts, image_specs = convert(image, BGR2RGB=False)
    print("len(frames), len(exts), exts[0]['delay_time']", len(frames), len(exts), exts[0]['delay_time'])
    write_gif(frames, 'Rotating_earth_new.gif', fps=12)
    write_gif(frames[0], 'earth.gif')
    
# Version history

1.0: first release

# Dependencies

You need to install numpy by:

    pip install numpy
