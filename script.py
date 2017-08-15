#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from glob import glob
from collections import namedtuple
from itertools import product
from sys import argv
from PIL import Image, ImageDraw, ImageFont

def write(char: str, font: ImageFont.FreeTypeFont):
    canvas = Image.new("L", (prop["size"]["width"], prop["size"]["height"]), 255) # grayscale, white bg
    ImageDraw.Draw(canvas).text((0, 0), char, font=font, fill="#000")
    canvas.save("{}/{}-{}.png".format(prop["output_dir"], font.getname()[0], char), "PNG")

with open(argv[1], "r") as rawprop:
    prop = json.load(rawprop)
fonts = [ImageFont.truetype(e, prop["size"]["font"]) for e in glob(prop["fonts"])]

with open(prop["charfile"], "r") as chars:
    for i in product(chars, fonts):
        print(i[0][0])
        write(i[0][0], i[1])
