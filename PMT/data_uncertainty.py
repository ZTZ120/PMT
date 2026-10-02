'''
数据不确定性计算
'''
from math import log
import numpy as np

#计算熵
def calculateH(p):
    H = 0
    for i in range(len(p)):
        #if p[i] == 0:
        if p[i]==0.0000e+00:
            H=H-1e-50*log(1e-50,2)
            #p[i]=1e-50
            #print(p[i])
        #print(p[i])
        else:
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
#p=[0.9,0.05,0.05]
#print(calculateG(p))