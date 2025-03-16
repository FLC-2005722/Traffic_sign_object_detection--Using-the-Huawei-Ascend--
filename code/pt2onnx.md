# pt2onnx

```python
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8n.pt')
    model = YOLO("path/to/yolov8n.pt")
    model.export(format='onnx', simplify=True, opset=13)
```

[ultralytics官方转换参数连接](https://docs.ultralytics.com/modes/export/#usage-examples)



| **Argument** |     **Type**     | **Default** |                       **Description**                        |
| :----------: | :--------------: | :---------: | :----------------------------------------------------------: |
|   `imgsz`    | `int` 或 `tuple` |    `640`    | 模型输入所需的图像尺寸。对于正方形图像，可以是一个整数，或者是一个元组 `(height, width)` 了解具体尺寸。 |
|    `half`    |      `bool`      |   `False`   | 启用 FP16（半精度）量化，在支持的硬件上减小模型大小并可能加快推理速度。 |
|  `dynamic`   |      `bool`      |   `False`   | 允许为ONNX 、TensorRT 和OpenVINO 导出动态输入尺寸，提高了处理不同图像尺寸的灵活性。 |
|  `simplify`  |      `bool`      |   `True`    | 简化了ONNX 输出的模型图。 `onnxslim`这可能会提高性能和兼容性。 |
|   `opset`    |      `int`       |   `None`    | 指定ONNX opset 版本，以便与不同的ONNX 解析器和运行时兼容。如果未设置，则使用最新的支持版本。 |
|    `nms`     |      `bool`      |   `False`   | 在支持的情况下，为导出模型添加非最大值抑制 (NMS)（请参阅导出格式），提高检测后处理效率。 |
|   `batch`    |      `int`       |     `1`     | 指定导出模型的批量推理大小，或导出模型将同时处理的图像的最大数量。 `predict` 模式。 |



| [ONNX](https://docs.ultralytics.com/zh/integrations/onnx/) | `onnx` | `yolo11n.onnx` | ✅    | `imgsz`, `half`, `dynamic`, `simplify`, `opset`, `nms`, `batch` |
| ---------------------------------------------------------- | ------ | -------------- | ---- | ------------------------------------------------------------ |