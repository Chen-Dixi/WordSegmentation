# WordSegmentation
自然语言处理与应用分词作业

## 分词软件基于 CRF++-0.58
#### 需要先安装，网盘地址：
链接:https://pan.baidu.com/s/1-BPjdA1s0Gb2Olwn0MUAdw  密码:gs8d
#### CRF++系统安装
- Requirements

C++ compiler (gcc 3.0 or higher)
- How to make
```bash
% ./configure 
% make
% su
% make install
```
#### 安装到Python
```bash
% python setup.py install
% 注：最后一步最好用pyhton2运行，python3会有各种各样的问题
```

## Run
- Requirements

需要训练好的分词模型，这里提供用北京大学的语料库训练的模型
链接:https://pan.baidu.com/s/1dzPof1V-iPwhGQQgx9IE7A  密码:3rqd

#### 运行参数  
- model：分词模型文件 
- inputfile：需要分词的文本 
- outputfile：分词结果输出地址

#### 脚本
```bash
python segment.py model/crf_model_pku data/pku_test.utf8 data/result/pku_test_result.utf8
```


