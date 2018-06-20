# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 10:45:13 2018

@author: dengfeiyang
"""
import jieba
seg_list = jieba.cut_for_search("同时如果你希望使用其它分词工具,那么你可以留意我之后的博客,我会在接下来的日子里发布其他有关内容", HMM=False)  # 搜索引擎模式
print(", ".join(seg_list))

