'''
蜕变测试结果
'''
class MTResult:
    #初始化
    def __init__(self,source_name,follow_image_p,source_c,follow_c,MT_result):
        #原始图像名称
        self.source_name=source_name
        #follow_image_p为衍生图像预测概率分布
        self.follow_image_p=follow_image_p
        #原始分类类别
        self.source_c=source_c
        #衍生分类类别
        self.follow_c = follow_c
        #MT结果:通过为1,不通过为0
        self.MT_result=MT_result
    #获取原始图像名称
    def getSourceName(self):
        return self.source_name
    #获取衍生图像预测概率分布
    def getFollowImageP(self):
        return self.follow_image_p
    #获取原始分类类别
    def getSourceC(self):
        return self.source_c
    # 获取衍生分类类别
    def getFollowC(self):
        return self.follow_c
    #获取MT结果
    def getMTResult(self):
        return self.MT_result