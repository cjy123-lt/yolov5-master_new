import torch

print(torch.__version__)  # 查看torch当前版本号

print(torch.version.cuda)  # 编译当前版本的torch使用的cuda版本号

print(torch.cuda.is_available())  # 查看当前cuda是否可用于当前版本的Torch，如果输出True，则表示可用

#返回当前设备索引
print(torch.cuda.current_device())
print(#返回GPU的数量
torch.cuda.device_count())

