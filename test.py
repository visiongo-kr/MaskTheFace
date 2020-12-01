import glob
import os
from PIL import Image
import random


def random_color():
    colorArr = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0,14)]
    return "#"+color

# path = r"E:\my_github\MaskTheFace\test_images\021_surgical.jpg"
# Image.open(path).convert('L').save(path)
for i in glob.glob(r"E:\my_github\MaskTheFace\test_images\mini_set"):
    os.popen('python mask_the_face.py --path "{}" --color "{}"'.format(i, random_color()))
