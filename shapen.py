# -*- coding: utf-8 -*-
"""
2.锐化
"""
from PIL import Image
import numpy as np
#打开图片
image = Image.open('doc/9381.png')

image = image.convert('L')#转灰度图



image = np.asarray(image)
print(image.shape)

#大于135像素转为255
image = (image > 135) * 255

image = Image.fromarray(image).convert('L')
image.show()
image.save('doc/9381_2.png')