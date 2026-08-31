

# Traffic_sign_object_detection (Using the Huawei Ascend)

本项目旨在基于改进版 YOLOv8，结合多种自研模块，实现交通标志目标检测，并支持在华为昇腾（Ascend 310/310B4）开发板上高效部署。

## 目录结构

```
├── code/
│   ├── dataset/                # 数据增强脚本
│   │   └── TT100k enhance.py
│   ├── model/                  # 网络结构改进模块
│   │   ├── block_c2f faster kan.py
│   │   ├── block_DCCAttention.py
│   │   └── block_LGAFB.py
│   ├── pt2onnx.py              # PyTorch转ONNX脚本
│   ├── pt2onnx.md              # 转ONNX说明
│   └── onnx2om.md              # ONNX转OM说明
├── model/
│   └── single_test/            # 各阶段模型文件
│       ├── 20240704_single_yolov8n.pt
│       ├── 20240909_single_yolov8n.onnx
│       └── 20240910_single_yolov8n.om
├── LICENSE
└── README.md
```

## 主要功能

- **数据增强**：支持多通道低照度模拟、噪声添加、HSV/YCrCb空间增强等，提升模型对复杂环境的鲁棒性。
- **模型结构改进**：提供 `block_c2f faster kan.py`、`block_DCCAttention.py`、`block_LGAFB.py` 等改进模块。
- **模型格式转换**：支持PyTorch→ONNX→OM全流程，便于在昇腾NPU部署。

## 环境依赖

- Python 3.8+
- torch、torchvision
- ultralytics>=8.0.0
- opencv-python
- pillow
- numpy
- 华为昇腾工具链（ATC）

## 数据增强用法

```bash
cd code/dataset
python TT100k\ enhance.py
# 默认处理 input_images 文件夹，输出到 output_images
```

## PyTorch转ONNX

详见 `code/pt2onnx.py` 和 `pt2onnx.md`，核心代码如下：

```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.export(format='onnx', simplify=True, opset=13)
```

## ONNX转OM（昇腾310/310B4）

详见 `code/onnx2om.md`，核心命令如下：

```bash
atc --mode 0 --model "yolov8n.onnx" --framework 5 --input_format "NCHW" \
    --input_shape "images:1,3,640,640" --output yolov8-det --output_type "FP32" \
    --host_env_os "linux" --host_env_cpu "aarch64" --soc_version "Ascend310B4"
```

如遇内存不足，可尝试：
```bash
export TE_PARALLEL_COMPILER=1
export MAX_COMPILE_CORE_NUMBER=1
```

## 改进模块简介

- **block_c2f faster kan.py**
- **block_DCCAttention.py**
- **block_LGAFB.py**


---

如需详细训练、推理、部署流程或遇到问题，欢迎提交 issue 或联系作者。
