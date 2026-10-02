'''
数据不确定性计算
'''
from math import log
import numpy as np

#计算熵
def calculateH(p):
    H = 0
    for i in range(len(p)):
       if p[i]==0.0000e+00:
           p[i]=1e-50
       H = H - p[i] * log(p[i], 2)
       #H = H - p[i] * logp[i]
    return H

#计算基尼杂质系数
def calculateG(p):
    G = 1
    for i in range(len(p)):
        G = G - p[i] * p[i]
    return G

#计算最大概率值
def calculatePMax(p):
    p_max=np.max(p)
    return p_max
