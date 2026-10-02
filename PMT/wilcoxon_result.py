'''
基于Wilcoxon的模型不确定性概率化蜕变测试结果
'''
class WilcoxonResult:
    #初始化
    def __init__(self,source_name,follow_image_p,stat,p_value,PMT_result):
        #原始图像名称
        self.source_name=source_name
        #follow_image_p为衍生图像预测概率分布的二维数组
        self.follow_image_p=follow_image_p
        #统计量
        self.stat=stat
        #统计P-value
        self.p_value=p_value
        #PMT结果:通过为1,不通过为0
        self.PMT_result=PMT_result
    #获取原始图像名称
    def getSourceName(self):
        return self.source_name
    #获取衍生图像预测概率分布的二维数组
    def getFollowImageP(self):
        return self.follow_image_p
    #获取统计量
    def getStat(self):
        return self.stat
    #获取P-value
    def getPValue(self):
        return self.p_value
    #获取PMT结果
    def getPMTResult(self):
        return self.PMT_result