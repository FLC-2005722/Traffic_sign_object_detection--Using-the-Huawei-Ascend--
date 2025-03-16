# onnx2om

**om是一种可以在华为昇腾开发版（Ascend310）NPU上运行加速的模型，想要利用好华为昇腾开发版的NPU算力就需要把模型进行相应的转换，转换成能够通过NPU加速的om模型**

```
atc \
  --mode 0 \
  --model "yolov8n.onnx" \
  --framework 5 \
  --input_format "NCHW" \
  --input_shape "images:1,3,640,640" \
  --output yolov8-det \
  --output_type "FP32" \
  --host_env_os "linux" \
  --host_env_cpu "aarch64" \
  --soc_version "Ascend310B4"
```

通过atc工具对模型进行转换

```
--mode 设置为0, 含义为离线转换om模型
--model 设置为你需要转换的onnx模型
--framework 0:Caffe; 1:MindSpore; 3:Tensorflow; 5:Onnx, 我用的是onnx所以选5
--input_format 输入的数据格式, onnx的话默认就是NCHW格式
--input_shape 输入的数据形状, 格式是 "输入名:N,C,H,W"
--output 输出om模型的前缀名, 会自动补一个".om"后缀
--output_type 输出的数据类型, 可以选 "FP32" "FP16" 等, 根据你的需求来即可
--host_env_os 执行模型端的环境, 刷机的话应该都是linux
--host_env_cpu 执行模型端的cpu, 是aarch64架构的
--soc_version 这个是需要自己添加, AIpro的npu就是 "Ascend310B4"
```

> [!CAUTION]
>
> 由于华为昇腾开发版的内存限制，在执行atc工具转换时候可能会出现内存不够导致的错误，可以尝试执行下面的代码
>
> ```
>export TE_PARALLEL_COMPILER=1 
> export MAX_COMPILE_CORE_NUMBER=1
> ```
> 
> 执行完毕后可以再次尝试使用atc转换



> [!IMPORTANT]
>
> 由于Ascend算子的一些缘故，在转换过程中可能会遇到一系列的算子不匹配问题，可以查询官方的文档进行调整



[如何基于香橙派AIpro将开源框架模型转换为昇腾模型](https://www.hiascend.com/forum/thread-0276148114436453009-1-1.html)

[香橙派AIpro开源样例代码](https://gitee.com/ascend/EdgeAndRobotics)

[昇腾文档中心](https://www.hiascend.com/zh/document)

[香橙派AIpro学习资源一站式导航](https://www.hiascend.com/forum/thread-0285140173361311056-1-1.html)







------

与模型转换无关，作者的一些吐槽吧

> 谈一谈我自己对华为昇腾的看法吧！
>
> 
>
> 只能说还有很长的路要走啊，现在很多问题都是没有解决，虽然论坛服务以及回复很活跃（相比于国内的其他芯片厂家：瑞芯微），文档很详细但是只能说不太适合新手。想要建立自己的生态太难了，上手一点都不容易，很多东西要摸索很久，而且很多报错不是官方文档有解释的。网上资料很少，适合那些愿意专研的人，适合那些有时间的人。只能说害~加油吧。
