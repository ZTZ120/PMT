'''
指定路径保存排序后的原始图像以及执行后的信息->excel文件
'''
import argparse
import os

import main_PMT

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    #原始图像文件夹"~/route"
    parse.add_argument('--image_folder_route',type=str,default='',required=True,help='image_folder_route')
    #基于数据不确定性的排序方式
    parse.add_argument('--sort_type',type=str,default='H',required=True,choices=['H','G','PMax'],help='sort_type')
    #排序后信息的保存excel绝对路径
    parse.add_argument('--excel_route',type=str,default='',required=True,help='excel_route')
    #被测程序的绝对路径
    parse.add_argument('--object_program',type=str,default='',required=True,help='object_program')
    opt,_=parse.parse_known_args()
    #excel文件夹和文件名称
    excel_folder_route,excel_name=os.path.split(opt.excel_route)
    # 创建excel文件夹
    if not os.path.exists(excel_folder_route):
        os.makedirs(excel_folder_route)
    #调用原始图像排序函数
    main_PMT.sort_PMT(opt.image_folder_route,opt.sort_type,opt.excel_route,opt.object_program)
#python get_sort_source_image.py --image_folder_route "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/image" --sort_type H --excel_route "E:/rrrr.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/Xception.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/Xception/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/Xception/sort_H_Xception.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/Xception.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/VGG16/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG16/sort_H_VGG16.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/VGG16.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/VGG19/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/VGG19/sort_H_VGG19.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/VGG19.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/ResNet50/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/ResNet50/sort_H_ResNet50.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/ResNet50.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/InceptionV3/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/InceptionV3/sort_H_InceptionV3.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/InceptionV3.py"
#python get_sort_source_image.py --image_folder_route "E:/研究生/a实验室/毕业设计/实验结果/MobileNet/test" --sort_type H --excel_route "E:/研究生/a实验室/毕业设计/实验结果/MobileNet/sort_H_MobileNet.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/MobileNet.py"