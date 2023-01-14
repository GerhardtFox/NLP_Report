#### 各个文件夹说明

- dataset：主要用于存放数据集与训练用的词表库（大约1.8G，没放上去）内容如下：
  - tokens_list_en.pt
  - tokens_list_zh.pt
  - train.en
  - train.zh
  - vocab_en.pt
  - vocab_zh.pt

[百度网盘地址](https://pan.baidu.com/s/1iCbIqzPC8LxsaIr49TJ1dA?pwd=0709 )[提取码：0709]



- model/transformer_checkpoints：主要用于保存训练数据，主要内容如下

  - model_5000.pt
  - model_10000.pt
  - model_15000.pt
  - model_20000.pt
  - model_25000.pt
  - model_30000.pt
  - model_35000.pt
  - model_40000.pt
  - model_45000.pt
  - model_50000.pt
  - model_55000.pt
  - model_60000.pt
  
  [百度网盘地址](https://pan.baidu.com/s/1bE2QlsVIstkp7MRozNMojg?pwd=0709 )[提取码：0709]

由于自己笔记跑一个epoch太长，五六十个小时，我只训练了十几个小时，在batch_size=32的前提下，每5000个batch_size保存一次，训练到60000.pt就结束了，用的这个版本做的预测。

当然在云服务器跑完了一个完整的epoch，报告最后有结果展示。



- runs/transformer_loss：存放损失函数的数据记录

  

- 报告中的小练习：主要是在用Transformer做翻译的前，找了一个小案例-CopyTask，作为练手的小项目，报告中有介绍。

  

- Transforme_MT.ipynb：代码文件，按照网上的教程，自己做注释理解敲了一遍，并修正了一些版本不兼容的问题。# NLP_Report
