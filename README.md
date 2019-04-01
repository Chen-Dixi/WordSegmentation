# WordSegmentation
自然语言处理与应用分词作业 基于条件随机场原理，对隐马尔可夫模型进行了改进。隐马尔可夫分词讲解：https://www.jianshu.com/p/f140c3a44ab6


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

需要训练好的分词模型，这里提供自己用北京大学的语料库训练的模型
链接:https://pan.baidu.com/s/1dzPof1V-iPwhGQQgx9IE7A  密码:3rqd

#### 运行参数  
- model：分词模型文件 
- inputfile：需要分词的文本 
- outputfile：分词结果输出地址

#### 脚本
```bash
python segment.py model/crf_model_pku data/pku_test.utf8 data/result/pku_test_result.utf8
```

#### Train
- 训练自己的语料库，语料库格式如下，词语之间用空格` `隔开
> “  人们  常  说  生活  是  一  部  教科书  ，  而  血  与  火  的  战争  更  是  不可多得  的  教科书  ，  她  确实  是  名副其实  的  ‘  我  的  大学  ’  。
“  心  静  渐  知  春  似  海  ，  花  深  每  觉  影  生  香  。
“  吃  屎  的  东西  ，  连  一  捆  麦  也  铡  不  动  呀  ？
他  “  严格要求  自己  ，  从  一个  科举  出身  的  进士  成为  一个  伟大  的  民主主义  者  ，  进而  成为  一  位  杰出  的  党外  共产主义  战士  ，  献身  于  崇高  的  共产主义  事业  。
......

- 训练脚本
```bash
python train_corpus.py data/template data/msr_training.utf8 model/msr_model
```
得到的模型文件`model/msr_model`可以用来进行新的分词任务

