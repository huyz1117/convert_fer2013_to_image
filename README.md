## fer2013人脸表情数据集

- fer2013人脸表情识别数据集由35887张人脸表情灰度图组成，图片大小为48x48，其中训练集28709张，测试集3589张，验证集3589张
- 共七种表情，分别对应于标签0-6，0代表`Anger`、1代表`Disgust`、2代表`Fear`、3代表`Happy`、4代表`Sad`、5代表`Superised`、6代表`Neutral`
- 官方数据集没有直接给出图片，而是将表情、像素、用途保存到csv文件中
- 可以使用`pandas解析数据，再将原始图片数据保存`jpg`图片

### Reference

- 数据集官网下载：[Kaggle](<https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data>)
- <https://blog.csdn.net/rookie_wei/article/details/83659595>