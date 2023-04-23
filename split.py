# -*- coding: utf-8 -*-
"""
3.分割图形并分类保存
"""

import numpy as np
import uuid
import os

from PIL import Image

# 图片阈值切割
def splitSingle(filename):
    pix = np.array(Image.open(filename).convert('L'))
    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]

    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        im = Image.fromarray(np.uint8(letter))

        save_path = './letters/' + str(uuid.uuid4()) + '.png'
        print('\t', save_path)

# 切割图片、保存
def splitAndSave(path):
    path = './source/' + path
    pix = np.array(Image.open(path).convert('L'))

    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]

    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        im = Image.fromarray(np.uint8(letter))
        save_path = './letters/' + str(uuid.uuid4()) + '.png'
        print('\t', save_path)
        im.save(save_path)


if __name__ == '__main__':
    im_paths = filter(lambda fn: os.path.splitext(fn)[1].lower() == '.png',
                      os.listdir('./source'))

    for im_path in im_paths:
        print(im_path)
        splitAndSave(im_path)
