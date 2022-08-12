# MIT License
# Copyright (c) 2020 h3ky1

# https://stackoverflow.com/questions/39936706/how-to-display-encrypted-image-as-an-image-without-decrypting-it

# Standard library imports
import base64
import math
import io

# Third party imports
from PIL import Image
# Local application imports

input_filename = '../data/frankenstein.hex'

# read message from file utf8
input_file = io.open(input_filename, mode="r", encoding="utf-8")
content = input_file.read().encode("ascii")
input_file.close()

with open("../data/frankenhex.bytes", "wb") as fh:
    fh.write(base64.decodebytes(content))

another_file = io.open("../data/frankenhex.bytes", mode="rb")
cyphertext = another_file.read()
another_file.close()

# calculate sizes
num_bytes = len(cyphertext)
num_pixels = int((num_bytes + 2) / 3)                 # 3 bytes per pixel
W = H = int(math.ceil(num_pixels ** 0.5))             # W=H, such that everything fits in

# fill the image with zeros, because probably len(imagedata) < needed W*H*3
imagedata = cyphertext + b'\0' * (W * H * 3 - len(cyphertext))
image = Image.frombytes('RGB', (W, H), imagedata)     # create image
image.save('../data/frankenimage.bmp')                # save to a file
