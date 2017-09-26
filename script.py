#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
from glob import glob
from itertools import product
from sys import argv
from PIL import Image, ImageDraw, ImageFont


def write(char, font):
    canvas = Image.new("L", (prop["size"]["width"], prop["size"]["height"]), 255) # grayscale, white bg
    ImageDraw.Draw(canvas).text((0, 0), char[1][0], font=font[1], fill="#000")
    output = "{0}/{1:04d}_{2}".format(prop["output_dir"], char[0], char[1][0])
    os.makedirs(output, mode=0o777, exist_ok=True)
    canvas.save("{0}/image{1:02d}.png".format(output, font[0]), "PNG")

with open(argv[1], "r") as rawprop:
    prop = json.load(rawprop)
fonts = [ImageFont.truetype(e, prop["size"]["font"]) for e in glob(prop["fonts"])]

with open(prop["charfile"], "r", encoding='utf-8') as chars:
    for i in product(enumerate(chars, start=1), enumerate(fonts, start=1)):
        print(i[0][1][0])
        write(i[0], i[1])
