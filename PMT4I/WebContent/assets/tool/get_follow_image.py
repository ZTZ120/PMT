'''
指定路径生成并保存衍生图像
'''
import argparse

import os

import cv2
import numpy as np

import main_PMT

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    #原始图像绝对路径
    parse.add_argument('--source_image_route',type=str,default='',required=True,help='source_image_route')
    #衍生图像绝对路径
    parse.add_argument('--follow_image_route',type=str,default='',required=True,help='follow_image_route')
    parse.add_argument('--MR',type=int,default=1,required=True,choices=range(1,13),help='MR')
    parse.add_argument('--param',type=int,default=1,required=True,choices=range(1,6),help='param')
    opt,_=parse.parse_known_args()
    follow_image_route=opt.follow_image_route
    #衍生图像的文件夹和文件名称
    follow_image_folder_route,follow_image_name=os.path.split(follow_image_route)
    #创建衍生图像文件夹
    if not os.path.exists(follow_image_folder_route):
        os.makedirs(follow_image_folder_route)
    # 允许中文的读取图片方式，参数1代表彩色图片忽略alpha通道读入
    source_image = cv2.imdecode(np.fromfile(opt.source_image_route, dtype=np.uint8), 1)
    # 调用生成衍生图片函数
    follow_images = main_PMT.getImage(source_image, opt.MR, opt.param,"Jaccard")
    #保存衍生图像
    cv2.imencode('.jpg', follow_images[0])[1].tofile(follow_image_route)
#python get_follow_image.py --source_image_route "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/image/test/ILSVRC2012_val_00000028.JPEG" --follow_image_route E:/rrrr.jpg --MR 1 --param 3