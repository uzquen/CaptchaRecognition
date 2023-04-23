# -*- coding: utf-8 -*-
"""
5.knn模型的test检验
"""
import numpy as np
import os

from PIL import Image
import joblib


def split_letters(path):
    pix = np.array(Image.open(path).convert('L'))
    # 阈值分割图片
    pix = (pix > 135) * 255

    split_parts = [
        [7, 16],
        [20, 29],
        [33, 42],
        [46, 55]
    ]
    letters = []
    for part in split_parts:
        letter = pix[7:, part[0]: part[1]]
        letters.append(letter.reshape(9*13))
    return letters

#获得验证码结果
def get_captcha_result(model_path, filename):
    sipo_knn = joblib.load(model_path)
    letters = split_letters(filename)
    return sipo_knn.predict(letters)

#批量打印test中的验证码图片
if __name__ == "__main__":
    for test in os.listdir('./test'):
        print(get_captcha_result('sipoknn.job', './test/' + test))
