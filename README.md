# 验证码识别

  

## 1.获取验证码
参考get_captcha.py，使用request对图片进行爬取.

## 2.锐化
参考shapen.py，对获取的图片进行锐化.

## 3.分割图形并保存
参考split.py，对锐化后图片进行分割以及分类保存.

## 4.搭建knn分类器
参考recognition.py，搭建knn分类器.

## 5. knn分类器测试
参考sipoknn.py，测试搭好的knn分类器.

## 6. 训练以及储存训练模型
参考train_and_dump.py，对图片进行识别训练.
