# -*- coding: utf-8 -*-
"""
4.搭建knn分类器、预测数据
"""


from PIL import Image
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#装载图片数据
def load_dataset():
    X = []
    y = []

    for i in range(70):
        path = "./train/%d%d.png" % (i / 7, i % 7)
        pix = np.asarray(Image.open(path).convert("L"))
        X.append(pix.reshape(9*13))
        y.append(int(i / 7))
    return np.asarray(X), np.asarray(y)

 # 切割数字
def split_letters(path):
    pix = np.asarray(Image.open(path).convert('L'))
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


if __name__ == "__main__":
    X, y = load_dataset()
    knn = KNeighborsClassifier()
    knn.fit(X, y)

    letters = split_letters('./test/test1.png')#选择图片
    print(knn.predict(letters))
