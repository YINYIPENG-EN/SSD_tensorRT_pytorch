```
git clone https://github.com/YINYIPENG-EN/SSD_tensorRT_pytorch.git
```

将权重下载后放置在model_data/下

权重：

链接：https://pan.baidu.com/s/1YAF_cruDG254ZZD5InPsbg 
提取码：yypn

# 1.torch转onnx

修改torch2onnx.py下权重路径以及类别【num_classes = 总classes+1】

网络输入大小。

可开启simplity功能

运行torch2onnx.py即可在model_data/下得到onnx文件

# 2.onnx推理

将ssd.py中的model_path修改为onnx路径，修改input_shape，将ONNX设置为True

图像检测：

运行predict.py，输入图像即可推理。

视频推理：

运行video.py即可

# 3.onnx转engine

修改onnx2trt.py中的onnx_file_path以及engin_file_path路径

运行onnx2trt.py文件，将会在model_data下得到ssd.engine文件

# 4.engine推理

将ssd.py中的model_path修改为engine路径，修改input_shape，将TRT设置为True

图像检测：

运行predict.py，输入图像即可推理。

视频推理：

运行video.py即可

# 5.pth or pt推理

将ssd.py中的model_path修改为torch权重路径，修改input_shape，将TRT和ONNX设置为False

图像检测：

运行predict.py，输入图像即可推理。

视频推理：

运行video.py即可



# 6.FPS测试

这里以测试engine为例。

将ssd.py中的model_path修改为engine路径，将TRT设置为True，将FPS_test.py中的TORCH设置为False.

运行FPS_test.py即可

这里我以我的1650显卡为例，测试效果如下

```
# engine:300*300 41FPS
# onnx:300*300 4FPS
# torch:300*300 28FPS
```

有问题请留言