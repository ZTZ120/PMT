'''
概率化蜕变测试方法
'''
import datetime
import os
import sys
import numpy as np
import cv2
import xlrd
import xlwt

import data_uncertainty
import mt_result
import source_image
import wilcoxon_result
import jaccard_result

import scipy.stats as ss

#import待测文件主程序
def importTest(file_folder,file_name):
    if not file_folder in sys.path:
        sys.path.append(file_folder)
    global test
    test = __import__(file_name)

#原始图像根据数据不确定性排序
def sort(image_folder_route,sort_type):
    # 遍历文件夹内所有图片路径,获取所有原始图像绝对路径
    test_routes=[]
    all = os.walk(image_folder_route)
    for path, dir, file_list in all:
        for file_name in file_list:
            if file_name.endswith('jpg') or file_name.endswith('png') or file_name.endswith('JPEG'):
                #图像绝对路径
                image_route = os.path.join(path,file_name)
                test_routes.append(image_route)
    sort_source_image=[]
    # 日期
    date_start = datetime.datetime.now()
    # 所有原始图像的预测概率分布二维数组
    ps=test.testAPI(test_routes)
    # 日期
    date_end = datetime.datetime.now()
    date_delta_API = (date_end - date_start).total_seconds() * 1000
    #print(ps)
    for i in range(len(ps)):
        print("sort读取所有原始图像的预测概率分布:",i)
        #原始预测概率分布
        p=ps[i]
        #print(p)
        # 熵
        H = data_uncertainty.calculateH(p)
        # print("H:",H)
        # 基尼杂质系数
        G = data_uncertainty.calculateG(p)
        # print("G:",G)
        # 最大概率值
        p_max = data_uncertainty.calculatePMax(p)
        # print("p_max:",p_max)
        #添加原始图像及运行结果信息
        source = source_image.SourceImage(test_routes[i], p, H, G, p_max)
        sort_source_image.append(source)
    #排序
    quickSort(sort_source_image,0,len(sort_source_image)-1,sort_type)
    return (sort_source_image,date_delta_API)

#快速排序(从大到小)
def quickSort(sort_source_image,start,end,sort_type):
    if start>=end:
        return
    temp=sort_source_image[start]
    i=start
    j=end
    while i<j:
        while i<j and sort_source_image[j].getDataUncertainty(sort_type)<temp.getDataUncertainty(sort_type):
            j=j-1
        if i<j:
            sort_source_image[i]=sort_source_image[j]
            i=i+1
        while i<j and sort_source_image[i].getDataUncertainty(sort_type)>temp.getDataUncertainty(sort_type):
            i=i+1
        if i<j:
            sort_source_image[j]=sort_source_image[i]
            j=j-1
    sort_source_image[i]=temp
    quickSort(sort_source_image,start,i-1,sort_type)
    quickSort(sort_source_image,i+1,end,sort_type)

#排序后的图像顺序记录在excel中
def sort_PMT(image_folder_route,sort_type,excel_route,object_program):
    # 日期
    date_start = datetime.datetime.now()
    # 被测程序的文件夹和文件名称
    file_folder, file_name = os.path.split(object_program)
    #被测程序文件名称的前后缀
    file_name, ext = os.path.splitext(file_name)
    # print(file_folder)
    # print(file_name)
    # import待测文件主程序
    importTest(file_folder, file_name)
    #原始图像排序
    sort_source_image,date_delta_API = sort(image_folder_route, sort_type)
    #excel记录
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    headers = ['0-被测文件路径', '1-图像文件夹路径','2-图像路径', '3-排序方式', '4-原始预测概率分布', '5-熵','6-基尼杂质系数', '7-1-最大概率', '8-起始时间', '9-结束时间', '10-时间开销','11-API时间开销']
    # excel头部标题
    for col, header in enumerate(headers):
        sheet.write(0, col, header)
    #写表
    for i in range(len(sort_source_image)):
        sheet.write(i+1, 0, object_program)
        sheet.write(i+1, 1, image_folder_route)
        sheet.write(i+1, 2, sort_source_image[i].getImageRoute())
        sheet.write(i+1, 3, sort_type)
        sheet.write(i+1, 4, ','.join(map(str,sort_source_image[i].getP())))
        sheet.write(i+1, 5, str(sort_source_image[i].getDataUncertainty("H")))
        sheet.write(i+1, 6, str(sort_source_image[i].getDataUncertainty("G")))
        sheet.write(i+1, 7, str(sort_source_image[i].getDataUncertainty("PMax")))
    # 日期
    date_end = datetime.datetime.now()
    date_delta = (date_end - date_start).total_seconds() * 1000
    sheet.write(1, 8, str(date_start))
    sheet.write(1, 9, str(date_end))
    sheet.write(1, 10, str(date_delta))
    sheet.write(1, 11, str(date_delta_API))
    # excel日志保存
    book.save(excel_route)
    # 删除import的待测文件主程序
    del sys.modules[file_name]

'''
#原本的算法思路,由于被测程序Model初始化次数=测试图像数量,导致运行时间越来越慢,性能很差,基本30+图像程序就会崩溃,因此优化程序运行方式,但整体逻辑不变
#概率化蜕变测试
def PMT(MRs,params,read_excel_route,excel_route,probabilistic_type):
    #读入原始图像以及部分测试信息
    read_book = xlrd.open_workbook(read_excel_route)
    read_sheet = read_book.sheet_by_index(0)
    object_program=read_sheet.cell_value(1,0)
    sort_type=read_sheet.cell_value(1,3)
    image_folder_route=read_sheet.cell_value(1,1)
    # 被测程序的文件夹和文件名称
    file_folder, file_name = os.path.split(object_program)
    #被测程序文件名称的前后缀
    file_name, ext = os.path.splitext(file_name)
    # print(file_folder)
    # print(file_name)
    # import待测文件主程序
    importTest(file_folder, file_name)
    # 原始图像排序,原本的方式,由于运行过程不能体现优先级排序方法的用户体验,已修改
    # sort_source_image=sort(image_folder_route,sort_type)
    sort_source_image = []
    #excel总行数
    rows=read_sheet.nrows
    #遍历所有原始图像信息
    for i in range(1,rows):
        #图像绝对路径
        image_route=read_sheet.cell_value(i,2)
        # 预测概率分布数组
        p_str=read_sheet.cell_value(i,4)
        p = p_str.split(',')
        for j in range(len(p)):
            p[j] = float(p[j])
        # 熵
        H=float(read_sheet.cell_value(i,5))
        # 基尼杂质系数
        G=float(read_sheet.cell_value(i,6))
        # 最大概率
        p_max=1-float(read_sheet.cell_value(i,7))
        #新增原始图像
        source=source_image.SourceImage(image_route,p,H,G,p_max)
        sort_source_image.append(source)
    #print(sort_source_image[0].getImageRoute())
    #print(sort_source_image[1].getImageRoute())
    #excel日志
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    headers = ['0-日期','1-被测文件名称','2-MR','3-param','4-概率化类型','5-排序方式','6-图像名称','7-PMT结果','8-原始预测概率分布','9-熵','10-基尼杂质系数','11-1-最大概率']
    # 循环所有MRs和params,执行PMT
    image_number=0
    #日期
    date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #根据概率化方式执行测试方法
    if probabilistic_type=="Wilcoxon":
        # wilcoxon样本数量
        sum = 20
        # excel头部标题
        headers.append('12-wilcoxon统计量')
        headers.append('13-P-value')
        now=14
        for i in range(sum):
            headers.append(str(now+i)+'-衍生预测概率分布'+str(i))
        for col,header in enumerate(headers):
            sheet.write(0,col,header)
        # 循环所有MRs和params,执行PMT
        for i in range(len(sort_source_image)):
            for j in range(len(MRs)):
                #图像数量
                image_number+=1
                #获得PMT结果
                result=probabilisticWilcoxon(image_folder_route,sort_source_image[i],MRs[j],params[j],sum)
                #写excel
                sheet.write(image_number, 0, date)
                sheet.write(image_number, 1, file_name)
                sheet.write(image_number, 2, str(MRs[j]))
                sheet.write(image_number, 3, str(params[j]))
                sheet.write(image_number, 4, probabilistic_type)
                sheet.write(image_number, 5, sort_type)
                sheet.write(image_number, 6, result.getSourceName())
                sheet.write(image_number, 7, str(result.getPMTResult()))
                sheet.write(image_number, 8, ','.join(map(str,sort_source_image[i].getP())))
                sheet.write(image_number, 9, str(sort_source_image[i].getDataUncertainty("H")))
                sheet.write(image_number, 10, str(sort_source_image[i].getDataUncertainty("G")))
                sheet.write(image_number, 11, str(sort_source_image[i].getDataUncertainty("PMax")))
                sheet.write(image_number, 12, str(result.getStat()))
                sheet.write(image_number, 13, str(result.getPValue()))
                for k in range(sum):
                    sheet.write(image_number,14+k,','.join(map(str,result.getFollowImageP()[k])))
    elif probabilistic_type=="Jaccard":
        #excel头部标题
        headers.append('12-IoU')
        headers.append('13-衍生预测概率分布')
        for col,header in enumerate(headers):
            sheet.write(0,col,header)
        # 循环所有MRs和params,执行PMT
        for i in range(len(sort_source_image)):
            for j in range(len(MRs)):
                #图像数量
                image_number+=1
                #获得PMT结果
                result=probabilisticJaccard(image_folder_route,sort_source_image[i],MRs[j],params[j])
                #写excel
                sheet.write(image_number, 0, date)
                sheet.write(image_number, 1, file_name)
                sheet.write(image_number, 2, str(MRs[j]))
                sheet.write(image_number, 3, str(params[j]))
                sheet.write(image_number, 4, probabilistic_type)
                sheet.write(image_number, 5, sort_type)
                sheet.write(image_number, 6, result.getSourceName())
                sheet.write(image_number, 7, str(result.getPMTResult()))
                sheet.write(image_number, 8, ','.join(map(str,sort_source_image[i].getP())))
                sheet.write(image_number, 9, str(sort_source_image[i].getDataUncertainty("H")))
                sheet.write(image_number, 10, str(sort_source_image[i].getDataUncertainty("G")))
                sheet.write(image_number, 11, str(sort_source_image[i].getDataUncertainty("PMax")))
                sheet.write(image_number, 12, str(result.getIoU()))
                sheet.write(image_number, 13, ','.join(map(str,result.getFollowImageP())))
    #excel日志保存
    book.save(excel_route)
    # 删除import的待测文件主程序
    del sys.modules[file_name]

#基于Wilcoxon的概率化蜕变测试方法,image_folder_route="~/route"
def probabilisticWilcoxon(image_folder_route,sort_source_image,MR,param,sum=20):
    #原始图像绝对路径和分类标签c
    source_route=sort_source_image.getImageRoute()
    c=np.argmax(sort_source_image.getP())
    #原始图像文件夹和文件名称
    image_folder,image_name = os.path.split(source_route)
    #衍生图像路径文件夹
    follow_route = image_folder_route + '/MR' + str(MR)
    if os.path.exists(follow_route) == False:
        os.makedirs(follow_route)
    follow_route = follow_route + '/' + str(param)
    if os.path.exists(follow_route) == False:
        os.makedirs(follow_route)
    #读取原始图像
    source_image=cv2.imdecode(np.fromfile(source_route, dtype=np.uint8), 1)
    #获取所有衍生图像
    follow_image=getImage(source_image,MR,param,"Wilcoxon")
    # 衍生图像预测概率分布二维数组
    follow_image_p=[]
    #原始图像最大概率值
    p1=sort_source_image.getPMax()
    #所有衍生图像对类别c的预测概率值数组
    p2=[]
    for i in range(sum):
        #保存衍生图像
        image_route = follow_route + '/' + str(i)
        if os.path.exists(image_route) == False:
            os.makedirs(image_route)
        image_route = image_route + '/' + image_name
        cv2.imencode('.jpg', follow_image[i])[1].tofile(image_route)
        #执行被测程序
        p=test.testAPI(image_route)
        follow_image_p.append(p)
        p2.append(p[c])
    #和原始图像预测概率值误差在0.05之内判定通过测试,避免相邻很近的概率值被wilcoxon统计结果判定不通过测试
    flag=1
    for i in range(len(p2)):
        if abs(p2[i]-p1)>=0.05:
            flag=0
            break
    if flag==1:
        result=wilcoxon_result.WilcoxonResult(image_name,follow_image_p,np.nan,1,1)
    else:
        repeat=[p1]*len(p2)
        #wilcoxon统计方法
        stat,p_value=ss.wilcoxon(p2,repeat,"zsplit",correction=True)
        #p_value<0.05则测试不通过
        PMT_result=1
        if p_value<0.05:
            PMT_result=0
        #保存测试结果信息
        result=wilcoxon_result.WilcoxonResult(image_name,follow_image_p,stat,p_value,PMT_result)
    return result

#基于Jaccard的概率化蜕变测试方法,image_folder_route="~/route"
def probabilisticJaccard(image_folder_route,sort_source_image,MR,param):
    #原始图像绝对路径
    source_route=sort_source_image.getImageRoute()
    #原始图像文件夹和文件名称
    image_folder,image_name = os.path.split(source_route)
    #衍生图像路径文件夹
    follow_route = image_folder_route + '/MR' + str(MR)
    if os.path.exists(follow_route) == False:
        os.makedirs(follow_route)
    follow_route = follow_route + '/' + str(param)
    if os.path.exists(follow_route) == False:
        os.makedirs(follow_route)
    #读取原始图像
    source_image=cv2.imdecode(np.fromfile(source_route, dtype=np.uint8), 1)
    #获取所有衍生图像
    follow_image=getImage(source_image,MR,param,"Jaccard")
    #保存衍生图像
    image_route = follow_route + '/' + image_name
    cv2.imencode('.jpg', follow_image[0])[1].tofile(image_route)
    #执行被测程序
    p2=test.testAPI(image_route)
    p1=sort_source_image.getP()
    #计算IoU
    I=0
    U=0
    for i in range(len(p2)):
        if p1[i]>p2[i]:
            I+=p2[i]
            U+=p1[i]
        else:
            I+=p1[i]
            U+=p2[i]
    IoU=I/U
    #IoU<0.75则测试不通过
    PMT_result=1
    if IoU<0.75:
        PMT_result=0
    #保存测试结果信息
    result=jaccard_result.JaccardResult(image_name,p2,IoU,PMT_result)
    return result'''

#概率化蜕变测试方法
def PMT(MRs,params,read_excel_route,excel_route,probabilistic_type,image_rows):
    # 日期
    date_start = datetime.datetime.now()
    #读入原始图像以及部分测试信息
    read_book = xlrd.open_workbook(read_excel_route)
    read_sheet = read_book.sheet_by_index(0)
    object_program=read_sheet.cell_value(1,0)
    sort_type=read_sheet.cell_value(1,3)
    image_folder_route=read_sheet.cell_value(1,1)
    # 被测程序的文件夹和文件名称
    file_folder, file_name = os.path.split(object_program)
    #被测程序文件名称的前后缀
    file_name, ext = os.path.splitext(file_name)
    # print(file_folder)
    # print(file_name)
    # import待测文件主程序
    importTest(file_folder, file_name)
    # 原始图像排序,原本的方式,由于运行过程不能体现优先级排序方法的用户体验,已修改
    # sort_source_image=sort(image_folder_route,sort_type)
    sort_source_images = []
    #excel总行数
    rows=read_sheet.nrows
    if image_rows>0 and image_rows<rows:
        rows=image_rows+1
    #遍历所有原始图像及运行结果信息
    for i in range(1,rows):
        #图像绝对路径
        image_route=read_sheet.cell_value(i,2)
        # 预测概率分布数组
        p_str=read_sheet.cell_value(i,4)
        p = p_str.split(',')
        for j in range(len(p)):
            p[j] = float(p[j])
        # 熵
        H=float(read_sheet.cell_value(i,5))
        # 基尼杂质系数
        G=float(read_sheet.cell_value(i,6))
        # 最大概率
        p_max=1-float(read_sheet.cell_value(i,7))
        #新增原始图像
        source=source_image.SourceImage(image_route,p,H,G,p_max)
        sort_source_images.append(source)
    #print(sort_source_image[0].getImageRoute())
    #print(sort_source_image[1].getImageRoute())
    #excel日志
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    headers = ['0-日期','1-被测文件名称','2-MR','3-param','4-概率化类型','5-排序方式','6-图像名称','7-PMT结果','8-原始预测概率分布','9-熵','10-基尼杂质系数','11-1-最大概率']
    # 循环所有MRs和params,执行PMT
    #日期
    date=date_start.strftime("%Y-%m-%d %H:%M:%S")
    #根据概率化方式执行测试方法
    if probabilistic_type=="Wilcoxon":
        # wilcoxon样本数量
        sum = 20
        # excel头部标题
        headers.append('12-wilcoxon统计量')
        headers.append('13-P-value')
        now=14
        for i in range(sum):
            headers.append(str(now+i)+'-衍生预测概率分布'+str(i))
        headers.append(str(14+sum) + '-起始时间')
        headers.append(str(15+sum) + '-结束时间')
        headers.append(str(16+sum) + '-时间开销')
        headers.append(str(17 + sum) + '-API时间开销')
        headers.append(str(18 + sum) + '-testCaseGeneration时间开销')
        for col,header in enumerate(headers):
            sheet.write(0,col,header)
        # 循环所有MRs和params,执行PMT
        results,date_delta_API,date_delta_generation=probabilisticWilcoxon(image_folder_route,sort_source_images,MRs,params,sum)
        for i in range(len(results)):
            #写excel
            sheet.write(i + 1, 0, date)
            sheet.write(i + 1, 1, file_name)
            sheet.write(i + 1, 2, str(MRs[i%len(MRs)]))
            sheet.write(i + 1, 3, str(params[i%len(MRs)]))
            sheet.write(i + 1, 4, probabilistic_type)
            sheet.write(i + 1, 5, sort_type)
            sheet.write(i + 1, 6, results[i].getSourceName())
            sheet.write(i + 1, 7, str(results[i].getPMTResult()))
            sheet.write(i + 1, 8, ','.join(map(str,sort_source_images[int(i/len(MRs))].getP())))
            sheet.write(i + 1, 9, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('H')))
            sheet.write(i + 1, 10, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('G')))
            sheet.write(i + 1, 11, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('PMax')))
            sheet.write(i + 1, 12, str(results[i].getStat()))
            sheet.write(i + 1, 13, str(results[i].getPValue()))
            for j in range(sum):
                sheet.write(i + 1, 14 + j, ','.join(map(str, results[i].getFollowImageP()[j])))
        # 日期
        date_end = datetime.datetime.now()
        date_delta = (date_end-date_start).total_seconds()*1000
        sheet.write(1, 14 + sum, str(date_start))
        sheet.write(1, 15 + sum, str(date_end))
        sheet.write(1, 16 + sum, str(date_delta))
        sheet.write(1, 17 + sum, str(date_delta_API))
        sheet.write(1, 18 + sum, str(date_delta_generation))
    elif probabilistic_type=="Jaccard":
        #excel头部标题
        headers.append('12-IoU')
        headers.append('13-衍生预测概率分布')
        headers.append('14-起始时间')
        headers.append('15-结束时间')
        headers.append('16-时间开销')
        headers.append('17-API时间开销')
        headers.append('18-testCaseGeneration时间开销')
        for col,header in enumerate(headers):
            sheet.write(0,col,header)
        # 循环所有MRs和params,执行PMT
        results,date_delta_API,date_delta_generation=probabilisticJaccard(image_folder_route,sort_source_images,MRs,params)
        for i in range(len(results)):
            #写excel
            sheet.write(i + 1, 0, date)
            sheet.write(i + 1, 1, file_name)
            sheet.write(i + 1, 2, str(MRs[i%len(MRs)]))
            sheet.write(i + 1, 3, str(params[i%len(MRs)]))
            sheet.write(i + 1, 4, probabilistic_type)
            sheet.write(i + 1, 5, sort_type)
            sheet.write(i + 1, 6, results[i].getSourceName())
            sheet.write(i + 1, 7, str(results[i].getPMTResult()))
            sheet.write(i + 1, 8, ','.join(map(str,sort_source_images[int(i/len(MRs))].getP())))
            sheet.write(i + 1, 9, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('H')))
            sheet.write(i + 1, 10, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('G')))
            sheet.write(i + 1, 11, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('PMax')))
            sheet.write(i + 1, 12, str(results[i].getIoU()))
            sheet.write(i + 1, 13, ','.join(map(str,results[i].getFollowImageP())))
        # 日期
        date_end = datetime.datetime.now()
        date_delta = (date_end - date_start).total_seconds() * 1000
        sheet.write(1, 14, str(date_start))
        sheet.write(1, 15, str(date_end))
        sheet.write(1, 16, str(date_delta))
        sheet.write(1, 17, str(date_delta_API))
        sheet.write(1, 18, str(date_delta_generation))
    elif probabilistic_type=="MT":
        #excel头部标题
        headers.append('12-原始分类类别')
        headers.append('13-衍生分类类别')
        headers.append('14-衍生预测概率分布')
        headers.append('15-起始时间')
        headers.append('16-结束时间')
        headers.append('17-时间开销')
        headers.append('18-API时间开销')
        headers.append('19-testCaseGeneration时间开销')
        for col,header in enumerate(headers):
            sheet.write(0,col,header)
        # 循环所有MRs和params,执行PMT
        results,date_delta_API,date_delta_generation=MT(image_folder_route,sort_source_images,MRs,params)
        for i in range(len(results)):
            #写excel
            sheet.write(i + 1, 0, date)
            sheet.write(i + 1, 1, file_name)
            sheet.write(i + 1, 2, str(MRs[i%len(MRs)]))
            sheet.write(i + 1, 3, str(params[i%len(MRs)]))
            sheet.write(i + 1, 4, probabilistic_type)
            sheet.write(i + 1, 5, sort_type)
            sheet.write(i + 1, 6, results[i].getSourceName())
            sheet.write(i + 1, 7, str(results[i].getMTResult()))
            sheet.write(i + 1, 8, ','.join(map(str,sort_source_images[int(i/len(MRs))].getP())))
            sheet.write(i + 1, 9, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('H')))
            sheet.write(i + 1, 10, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('G')))
            sheet.write(i + 1, 11, str(sort_source_images[int(i/len(MRs))].getDataUncertainty('PMax')))
            sheet.write(i + 1, 12, str(results[i].getSourceC()))
            sheet.write(i + 1, 13, str(results[i].getFollowC()))
            sheet.write(i + 1, 14, ','.join(map(str,results[i].getFollowImageP())))
        # 日期
        date_end = datetime.datetime.now()
        date_delta = (date_end - date_start).total_seconds() * 1000
        sheet.write(1, 15, str(date_start))
        sheet.write(1, 16, str(date_end))
        sheet.write(1, 17, str(date_delta))
        sheet.write(1, 18, str(date_delta_API))
        sheet.write(1, 19, str(date_delta_generation))
    #excel日志保存
    book.save(excel_route)
    # 删除import的待测文件主程序
    del sys.modules[file_name]

#基于Wilcoxon的概率化蜕变测试方法,image_folder_route="~/route"
def probabilisticWilcoxon(image_folder_route,sort_source_images,MRs,params,sum=20):
    test_routes = []
    results = []
    date_start_generation = datetime.datetime.now()
    # 循环所有MRs和params,执行PMT
    for i in range(len(sort_source_images)):
        print("Wilcoxon读取所有原始图像:", i)
        # 原始图像绝对路径
        source_route = sort_source_images[i].getImageRoute()
        # 原始图像文件夹和文件名称
        image_folder, image_name = os.path.split(source_route)
        # 读取原始图像
        source_image = cv2.imdecode(np.fromfile(source_route, dtype=np.uint8), 1)
        for j in range(len(MRs)):
            #衍生图像路径文件夹
            follow_route = os.path.abspath(os.path.join(image_folder_route, "..")) + '/Wilcoxon_MR' + str(MRs[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            follow_route = follow_route + '/' + str(params[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            #获取所有衍生图像
            follow_image=getImage(source_image,MRs[j],params[j],"Wilcoxon")
            for k in range(sum):
                #保存衍生图像
                image_route=follow_route+'/'+str(k)
                if os.path.exists(image_route) == False:
                    os.makedirs(image_route)
                image_route = image_route + '/' + image_name
                cv2.imencode('.jpg', follow_image[k])[1].tofile(image_route)
                #添加衍生图像绝对路径
                test_routes.append(image_route)
    date_end_generation = datetime.datetime.now()
    date_delta_generation = (date_end_generation - date_start_generation).total_seconds() * 1000
    # 日期
    date_start = datetime.datetime.now()
    #执行被测程序
    ps=test.testAPI(test_routes)
    # 日期
    date_end = datetime.datetime.now()
    date_delta_API = (date_end - date_start).total_seconds() * 1000
    #以sum为步进遍历所有执行结果
    for i in range(0,len(ps),sum):
        #衍生图像预测概率分布二维数组
        follow_image_p=[]
        # 分类标签c
        c = np.argmax(sort_source_images[int(int(i/sum)/len(MRs))].getP())
        #原始图像最大概率值
        p1=sort_source_images[int(int(i/sum)/len(MRs))].getPMax()
        #原始图像文件夹和文件名称
        image_folder, image_name = os.path.split(sort_source_images[int(int(i/sum)/len(MRs))].getImageRoute())
        p2=[]
        #遍历sum个衍生图像,获取衍生图像对类别c的预测概率值数组
        for j in range(i,i+sum,1):
            follow_image_p.append(ps[j])
            p2.append(ps[j][c])
        #和原始图像预测概率值误差在0.05之内判定通过测试,避免相邻很近的概率值被wilcoxon统计结果判定不通过测试
        flag=1
        for j in range(len(p2)):
            if abs(p2[j]-p1)>=0.05:
                flag=0
                break
        if flag==1:
            result=wilcoxon_result.WilcoxonResult(image_name,follow_image_p,np.nan,1,1)
        else:
            repeat=[p1]*len(p2)
            #wilcoxon统计方法
            stat,p_value=ss.wilcoxon(p2,repeat,"zsplit",correction=True)
            #p_value<0.05则测试不通过
            PMT_result=1
            if p_value<0.05:
                PMT_result=0
            #保存测试结果信息
            result=wilcoxon_result.WilcoxonResult(image_name,follow_image_p,stat,p_value,PMT_result)
        results.append(result)
    return (results,date_delta_API,date_delta_generation)

#基于Jaccard的概率化蜕变测试方法,image_folder_route="~/route"
def probabilisticJaccard(image_folder_route,sort_source_images,MRs,params):
    test_routes=[]
    results=[]
    date_start_generation = datetime.datetime.now()
    # 循环所有MRs和params,执行PMT
    for i in range(len(sort_source_images)):
        print("Jaccard读取所有原始图像:", i)
        #原始图像路径
        source_route=sort_source_images[i].getImageRoute()
        # 原始图像文件夹和文件名称
        image_folder, image_name = os.path.split(source_route)
        # 读取原始图像
        source_image = cv2.imdecode(np.fromfile(source_route, dtype=np.uint8), 1)
        for j in range(len(MRs)):
            #衍生图像路径文件夹
            follow_route = os.path.abspath(os.path.join(image_folder_route, "..")) + '/Jaccard_MR' + str(MRs[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            follow_route = follow_route + '/' + str(params[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            #获取所有衍生图像
            follow_image=getImage(source_image,MRs[j],params[j],"Jaccard")
            #保存衍生图像
            image_route = follow_route + '/' + image_name
            cv2.imencode('.jpg', follow_image[0])[1].tofile(image_route)
            #添加衍生图像绝对路径
            test_routes.append(image_route)
    date_end_generation = datetime.datetime.now()
    date_delta_generation = (date_end_generation - date_start_generation).total_seconds() * 1000
    # 日期
    date_start = datetime.datetime.now()
    #执行被测程序
    ps=test.testAPI(test_routes)
    # 日期
    date_end = datetime.datetime.now()
    date_delta_API = (date_end - date_start).total_seconds() * 1000
    #遍历所有执行结果
    for i in range(len(ps)):
        #衍生图像预测概率分布
        p2=ps[i]
        #原始图像预测概率分布
        p1=sort_source_images[int(i/len(MRs))].getP()
        #原始图像文件夹和文件名称
        image_folder,image_name=os.path.split(sort_source_images[int(i/len(MRs))].getImageRoute())
        #计算IoU
        I=0
        U=0
        for j in range(len(p2)):
            if p1[j]>p2[j]:
                I+=p2[j]
                U+=p1[j]
            else:
                I+=p1[j]
                U+=p2[j]
        IoU=I/U
        #IoU<0.75则测试不通过
        PMT_result=1
        if IoU<0.75:
            PMT_result=0
        #保存测试结果信息
        result=jaccard_result.JaccardResult(image_name,p2,IoU,PMT_result)
        results.append(result)
    return (results,date_delta_API,date_delta_generation)

#蜕变测试方法,image_folder_route="~/route"
def MT(image_folder_route,sort_source_images,MRs,params):
    test_routes=[]
    results=[]
    date_start_generation = datetime.datetime.now()
    # 循环所有MRs和params,执行MT
    for i in range(len(sort_source_images)):
        print("MT读取所有原始图像:", i)
        #原始图像路径
        source_route=sort_source_images[i].getImageRoute()
        # 原始图像文件夹和文件名称
        image_folder, image_name = os.path.split(source_route)
        # 读取原始图像
        source_image = cv2.imdecode(np.fromfile(source_route, dtype=np.uint8), 1)
        for j in range(len(MRs)):
            #衍生图像路径文件夹
            follow_route = os.path.abspath(os.path.join(image_folder_route, "..")) + '/MT_MR' + str(MRs[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            follow_route = follow_route + '/' + str(params[j])
            if os.path.exists(follow_route) == False:
                os.makedirs(follow_route)
            #获取所有衍生图像
            follow_image=getImage(source_image,MRs[j],params[j],"Jaccard")
            #保存衍生图像
            image_route = follow_route + '/' + image_name
            cv2.imencode('.jpg', follow_image[0])[1].tofile(image_route)
            #添加衍生图像绝对路径
            test_routes.append(image_route)
    date_end_generation = datetime.datetime.now()
    date_delta_generation = (date_end_generation - date_start_generation).total_seconds() * 1000
    # 日期
    date_start = datetime.datetime.now()
    #执行被测程序
    ps=test.testAPI(test_routes)
    # 日期
    date_end = datetime.datetime.now()
    date_delta_API = (date_end - date_start).total_seconds() * 1000
    #遍历所有执行结果
    for i in range(len(ps)):
        #衍生图像预测概率分布
        p2=ps[i]
        #原始图像预测概率分布
        p1=sort_source_images[int(i/len(MRs))].getP()
        #原始图像文件夹和文件名称
        image_folder,image_name=os.path.split(sort_source_images[int(i/len(MRs))].getImageRoute())
        #计算原始类别和衍生类别
        source_c=np.argmax(p1)
        follow_c=np.argmax(p2)
        #原始类别和衍生类别不同则测试不通过
        MT_result=1
        if source_c!=follow_c:
            MT_result=0
        #保存测试结果信息
        result=mt_result.MTResult(image_name,p2,source_c,follow_c,MT_result)
        results.append(result)
    return (results,date_delta_API,date_delta_generation)

#获得衍生测试用例
def getImage(source_image,MR,param,probabilistic_type,sum=20):
    #获得行和列数
    if len(source_image.shape) == 3:
        rows,cols,channel = source_image.shape
    else:
        rows,cols = source_image.shape
        channel = 2
    #返回的衍生图像数组
    follow_image = []
    if MR==1:
        #改变图像对比度,param(1,2,3,4,5):0.95,0.90,0.85,0.80,0.75
        blank = np.zeros(source_image.shape, source_image.dtype)
        alpha = 1.0-0.05*param
        beta = 0
        step=(1-alpha)/(sum/2)
        #根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range((int)(sum/2)):
                img=cv2.addWeighted(source_image,alpha,blank,1-alpha,beta)
                follow_image.append(img)
                alpha+=step
            for i in range((int)(sum/2)):
                alpha+=step
                img=cv2.addWeighted(source_image,alpha,blank,1-alpha,beta)
                follow_image.append(img)
        elif probabilistic_type=="Jaccard":
            img=cv2.addWeighted(source_image,alpha,blank,1-alpha,beta)
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==2:
        # 改变图像亮度,param(1,2,3,4,5):5,10,15,20,25
        blank = np.zeros(source_image.shape, source_image.dtype)
        alpha = 1
        beta = param * 5
        step = beta/sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                img=cv2.addWeighted(source_image,alpha,blank,1-alpha,beta)
                follow_image.append(img)
                beta-=step
        elif probabilistic_type=="Jaccard":
            img=cv2.addWeighted(source_image,alpha,blank,1-alpha,beta)
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==3:
        # 随机扰动噪声处理(高斯噪声模拟光照差异),param(1)
        mean = 0
        var = 0.01
        img_temp = np.array(source_image / 255, dtype=float)
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                noise=np.random.normal(mean,var**0.5,source_image.shape)
                img=img_temp+noise
                img=np.clip(img,0,1.0)
                img=np.uint8(img*255)
                follow_image.append(img)
        elif probabilistic_type=="Jaccard":
            noise=np.random.normal(mean,var**0.5,source_image.shape)
            img=img_temp+noise
            img = np.clip(img, 0, 1.0)
            img = np.uint8(img * 255)
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==4:
        # 仿射变换,param(1,2,3,4,5):0.01,0.02,0.03,0.04,0.05
        x=param*0.01
        step=x/sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                M1=np.float32([[0,0],[cols-1,0],[0,rows-1]])
                M2=np.float32([[0,0],[(cols-1)*(1-x),0],[(cols-1)*x,rows-1]])
                M=cv2.getAffineTransform(M1,M2)
                img=cv2.warpAffine(source_image,M,(cols,rows))
                follow_image.append(img)
                x-=step
        elif probabilistic_type=="Jaccard":
            M1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
            M2 = np.float32([[0, 0], [(cols - 1) * (1 - x), 0], [(cols - 1) * x, rows - 1]])
            M = cv2.getAffineTransform(M1, M2)
            img = cv2.warpAffine(source_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==5:
        # 图像微小平移,param(1,2,3,4,5):0.01,0.02,0.03,0.04,0.05
        # 列偏移量和行偏移量
        x = param * 0.01
        step=x/sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                M=np.float32([[1,0,x*cols],[0,1,0]])
                img=cv2.warpAffine(source_image,M,(cols,rows))
                follow_image.append(img)
                x-=step
        elif probabilistic_type=="Jaccard":
            M = np.float32([[1, 0, x * cols], [0, 1, 0]])
            img = cv2.warpAffine(source_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==6:
        # 图像微小旋转,param(1,2,3,4,5):1.6,1.8,2.0,2.2,2.4
        x = 1.4 + param * 0.2
        step=x/sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                M=cv2.getRotationMatrix2D((cols/2.0,rows/2.0),x,1)
                img=cv2.warpAffine(source_image,M,(cols,rows))
                follow_image.append(img)
                x-=step
        elif probabilistic_type=="Jaccard":
            M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
            img = cv2.warpAffine(source_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==7:
        # 图像微小放大,param(1,2,3,4,5):20,40,60,80,100
        # INTER_LINEAR双线性插值
        #x = max(param*sum / rows, param*sum / cols)
        x=param*0.01
        step=x/sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type=="Wilcoxon":
            for i in range(sum):
                img=cv2.resize(source_image,None,fx=1+x,fy=1+x,interpolation=cv2.INTER_LINEAR)
                follow_image.append(img)
                x-=step
        elif probabilistic_type=="Jaccard":
            img = cv2.resize(source_image, None, fx=1 + x, fy=1 + x, interpolation=cv2.INTER_LINEAR)
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==8:
        # 图像微小缩小,param(1,2,3,4,5):20,40,60,80,100
        #x = param * 0.01
        # INTER_LINEAR双线性插值
        #x = max(param * sum / rows, param * sum / cols)
        x=param*0.01
        step = x / sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type == "Wilcoxon":
            for i in range(sum):
                img = cv2.resize(source_image, None, fx=1 - x, fy=1 - x, interpolation=cv2.INTER_LINEAR)
                follow_image.append(img)
                x -= step
        elif probabilistic_type == "Jaccard":
            img = cv2.resize(source_image, None, fx=1 - x, fy=1 - x, interpolation=cv2.INTER_LINEAR)
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==9:
        #图像模糊+微小旋转
        #图像模糊
        middle_image=cv2.GaussianBlur(source_image, (3, 3), 0)#(5,5)
        # 图像微小旋转,param(1,2,3,4,5):1.6,1.8,2.0,2.2,2.4
        x = 1.4 + param * 0.2
        step = x / sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type == "Wilcoxon":
            for i in range(sum):
                M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
                img = cv2.warpAffine(middle_image, M, (cols, rows))
                follow_image.append(img)
                x -= step
        elif probabilistic_type == "Jaccard":
            M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
            img = cv2.warpAffine(middle_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==10:
        #改变图像锐度+微小旋转
        #改变图像锐度
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        middle_image = cv2.filter2D(source_image, -1, kernel)
        # 图像微小旋转,param(1,2,3,4,5):1.6,1.8,2.0,2.2,2.4
        x = 1.4 + param * 0.2
        step = x / sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type == "Wilcoxon":
            for i in range(sum):
                M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
                img = cv2.warpAffine(middle_image, M, (cols, rows))
                follow_image.append(img)
                x -= step
        elif probabilistic_type == "Jaccard":
            M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
            img = cv2.warpAffine(middle_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==11:
        # 图像微小侵蚀+微小旋转
        # MORPH_ELLIPSE表示椭圆形
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))#或(5,5)
        middle_image = cv2.erode(source_image, kernel, iterations=1)
        # 图像微小旋转,param(1,2,3,4,5):1.6,1.8,2.0,2.2,2.4
        x = 1.4 + param * 0.2
        step = x / sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type == "Wilcoxon":
            for i in range(sum):
                M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
                img = cv2.warpAffine(middle_image, M, (cols, rows))
                follow_image.append(img)
                x -= step
        elif probabilistic_type == "Jaccard":
            M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
            img = cv2.warpAffine(middle_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    elif MR==12:
        # 图像微小膨胀+微小旋转
        # MORPH_RECT表示矩形
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))#或(5,5)
        middle_image = cv2.dilate(source_image, kernel, iterations=1)
        # 图像微小旋转,param(1,2,3,4,5):1.6,1.8,2.0,2.2,2.4
        x = 1.4 + param * 0.2
        step = x / sum
        # 根据概率化方式生成衍生图像
        if probabilistic_type == "Wilcoxon":
            for i in range(sum):
                M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
                img = cv2.warpAffine(middle_image, M, (cols, rows))
                follow_image.append(img)
                x -= step
        elif probabilistic_type == "Jaccard":
            M = cv2.getRotationMatrix2D((cols / 2.0, rows / 2.0), x, 1)
            img = cv2.warpAffine(middle_image, M, (cols, rows))
            follow_image.append(img)
        else:
            follow_image.append(source_image)
    return follow_image

#PMT("E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/image","E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/object-program/Xception.py","","","","H","Wilcoxon")
'''img1 = cv2.imdecode(np.fromfile("E:/Program Files/PyCharm Community Edition 2020.1.1/projects/PMT4I/image/test/ILSVRC2012_val_00000028.JPEG", dtype=np.uint8), 1)
cv2.imshow("source",img1)
follow=getImage(img1,11,3,"Wilcoxon")
cv2.imshow("follow0", follow[0])
cv2.imshow("follow19", follow[19])
cv2.waitKey()
cv2.destroyAllWindows()'''
