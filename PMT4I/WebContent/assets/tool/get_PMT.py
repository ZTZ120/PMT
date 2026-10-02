'''
指定测试信息,执行PMT方法->保存至excel文件
'''
import argparse
import os

import main_PMT

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    #概率化方式
    parse.add_argument('--probabilistic_type',type=str,default='Wilcoxon',required=True,choices=['Wilcoxon','Jaccard','MT'],help='probabilistic_type')
    #保存测试结果的excel绝对路径
    parse.add_argument('--excel_route',type=str,default='',required=True,help='excel_route')
    #排序的原始图像信息的excel绝对路径
    parse.add_argument('--read_excel_route',type=str,default='',required=True,help='read_excel_route')
    #原始图像排序后选择执行测试的数量
    parse.add_argument('--image_rows', type=int, default=1, required=True, help='image_rows')
    parse.add_argument('--MR', type=int,default=1, required=True, choices=range(1, 13), nargs='*',help='MR')
    parse.add_argument('--param', type=int,default=1, required=True, choices=range(1, 6), nargs='*',help='param')
    opt,_=parse.parse_known_args()
    #保存excel的文件夹和文件名称
    excel_folder_route,excel_name=os.path.split(opt.excel_route)
    # 创建excel文件夹
    if not os.path.exists(excel_folder_route):
        os.makedirs(excel_folder_route)
    #print(opt)
    #调用概率化方法函数
    main_PMT.PMT(opt.MR,opt.param,opt.read_excel_route,opt.excel_route,opt.probabilistic_type,opt.image_rows)
#python get_PMT.py --probabilistic_type Wilcoxon --read_excel_route "E:/rrrr.xls" --excel_route "E:/Desktop/rrrr_Wilcoxon.xls" --image_rows 1000 --MR 1 2 --param 3 4
#python get_PMT.py --probabilistic_type Wilcoxon --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/Xception/sort_H_Xception.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/Xception/MR1-3_Wilcoxon_H.xls" --MR 1 --param 3
#python get_PMT.py --probabilistic_type Jaccard --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG16/sort_H_VGG16.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG16/MR1-3_Jaccard_H.xls" --MR 1 --param 3
#python get_PMT.py --probabilistic_type Jaccard --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG19/sort_H_VGG19.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG19/MR1-3_Jaccard_H.xls" --MR 1 --param 3
#python get_PMT.py --probabilistic_type Jaccard --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/ResNet50/sort_H_ResNet50.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/ResNet50/MR1-3_Jaccard_H.xls" --MR 1 --param 3
#python get_PMT.py --probabilistic_type Jaccard --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/InceptionV3/sort_H_InceptionV3.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/InceptionV3/MR1-3_Jaccard_H.xls" --MR 1 --param 3
#python get_PMT.py --probabilistic_type Jaccard --read_excel_route "E:/研究生/a实验室/毕业设计/实验结果/MobileNet/sort_H_MobileNet.xls" --excel_route "E:/研究生/a实验室/毕业设计/实验结果/MobileNet/MR1-3_Jaccard_H.xls" --MR 1 --param 3