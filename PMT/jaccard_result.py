'''
基于Jaccard的模型不确定性概率化蜕变测试结果
'''
class JaccardResult:
    #初始化
    def __init__(self,source_name,follow_image_p,IoU,PMT_result):
        #原始图像名称
        self.source_name=source_name
        #follow_image_p为衍生图像预测概率分布
        self.follow_image_p=follow_image_p
        #IoU
        self.IoU=IoU
        #PMT结果:通过为1,不通过为0
        self.PMT_result=PMT_result
    #获取原始图像名称
    def getSourceName(self):
        return self.source_name
    #获取衍生图像预测概率分布
    def getFollowImageP(self):
        return self.follow_image_p
    #获取IoU
    def getIoU(self):
        return self.IoU
    #获取PMT结果
    def getPMTResult(self):
        return self.PMT_result