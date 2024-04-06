import torch

# 检查 CUDA 是否可用（在 Apple Silicon 上应该返回 False）
cuda_available = torch.cuda.is_available()

if cuda_available:
    # CUDA 特定的代码
    device = torch.device("cuda")
else:
    # 使用 CPU 或其他可用的设备
    device = torch.device("cpu")

# 打印当前选择的设备
print("Using device:", device)

# 示例：使用确定的 device 来创建一个 tensor
tensor = torch.tensor([1, 2, 3], device=device)
print("Tensor on device:", tensor)
