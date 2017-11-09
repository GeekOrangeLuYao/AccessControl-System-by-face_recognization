# AccessControl-System-by-face_recognization
A homework stored just like a tring

## 检测部分
pytorch(需要Linux环境)

faster-cnn 跑 vgg16

> 此处鸣谢gcy

## 识别部分
暂时还是准备使用vgg16，最后得到特征向量，使用余弦定理进行比对即可

## 标准化操作
参看doc中间的标准化的代码，这个是一个传统的做法

## Api部分
Api部分是使用了EyeKey的Api实现的这个功能，使用urllib等库