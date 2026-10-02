'''
原始图像及运行结果信息
'''
class SourceImage:
    #初始化
    def __init__(self,image_route,p,H,G,p_max):
        #原始图像绝对路径
        self.image_route=image_route
        #预测概率分布数组
        self.p=p
        #熵
        self.H=H
        #基尼杂质系数
        self.G=G
        #最大概率值
        self.p_max=p_max
    #获取原始图像绝对路径
    def getImageRoute(self):
        return self.image_route
    #获取预测概率分布
    def getP(self):
        return self.p
    #获取熵
    def getH(self):
        return self.H
    #获取基尼杂质系数
    def getG(self):
        return self.G
    #获取最大概率值
    def getPMax(self):
        return self.p_max
    #根据排序使用的数据不确定性指标返回对应值,其中基于最大概率值的数据不确定性为1-p_max
    def getDataUncertainty(self,sort_type):
        if sort_type=="H":
            return self.H
        elif sort_type=="G":
            return self.G
        elif sort_type=="PMax":
            return 1-self.p_max
        else:
            return -1