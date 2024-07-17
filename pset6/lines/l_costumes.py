import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes1.gif", save_all=True, append_images=[images[1], images[2], images[3],
                                                    images[4], images[5], images[6]],
                                                      duration=120, loop=0
)
