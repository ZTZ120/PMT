'''
依据excel测试结果文件，分析RQ1-4实验数据
'''

import xlrd
import xlwt
import scipy.stats as ss
import numpy as np
import pandas as pd

object="Xception"
#read_excel_route是所有蜕变关系测试结果excel路径的数组
def dataAnalysisOne(read_excel_route,excel_route):
    PMT_results=[[0 for _ in range(1000)] for _ in range(len(read_excel_route)+1)]
    # 记录所有MR总的测试结果的头部
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    headers = ['0-','1-被测文件名称', '2-','3-','4-概率化类型', '5-排序方式', '6-图像名称', '7-PMT结果', '8-原始预测概率分布', '9-熵',
               '10-基尼杂质系数', '11-1-最大概率']
    for col, header in enumerate(headers):
        sheet.write(0, col, header)
    # 读入所有MR的测试结果
    for i in range(0,len(read_excel_route)):
        read_book = xlrd.open_workbook(read_excel_route[i])
        read_sheet = read_book.sheet_by_index(0)
        # excel总行数
        rows = read_sheet.nrows
        for j in range(1,rows):
            PMT_result=read_sheet.cell_value(j, 7)
            PMT_results[i][j-1]=int(PMT_result)
            #记录部分原始图像信息
            if i==0:
                sheet.write(j,1,read_sheet.cell_value(j, 1))
                sheet.write(j, 4, read_sheet.cell_value(j, 4))
                sheet.write(j, 5, read_sheet.cell_value(j, 5))
                sheet.write(j, 6, read_sheet.cell_value(j, 6))
                sheet.write(j, 8, read_sheet.cell_value(j, 8))
                sheet.write(j, 9, read_sheet.cell_value(j, 9))
                sheet.write(j, 10, read_sheet.cell_value(j, 10))
                sheet.write(j, 11, read_sheet.cell_value(j, 11))
    #统计所有MR总的测试结果
    for j in range(0,1000):
        for i in range(0,len(read_excel_route)):
            if PMT_results[i][j]==0:
                PMT_results[len(read_excel_route)][j]=0
                break
            else:
                PMT_results[len(read_excel_route)][j] = 1
    #记录所有MR总的测试结果
    for i in range(1000):
        # 写excel
        sheet.write(i + 1, 7, PMT_results[len(read_excel_route)][i])
    # excel日志保存
    book.save(excel_route)
    return PMT_results

def dataAnalysisTwo():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    read_excel_route_MT=["/mnt/c/resultstime/"+object+"/MR1-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_MT_H.xls"]
    read_excel_route_Jaccard=["/mnt/c/resultstime/"+object+"/MR1-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Jaccard_H.xls"]
    read_excel_route_Wilcoxon=["/mnt/c/resultstime/"+object+"/MR1-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Wilcoxon_H.xls"]
    PMT_results_MT=dataAnalysisOne(read_excel_route_MT,"/mnt/c/resultstime/"+object+"/MR-all_MT_H.xls")
    PMT_results_Jaccard=dataAnalysisOne(read_excel_route_Jaccard,"/mnt/c/resultstime/"+object+"/MR-all_Jaccard_H.xls")
    PMT_results_Wilcoxon=dataAnalysisOne(read_excel_route_Wilcoxon,"/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_H.xls")
    print("MT-VR")
    for i in range(len(PMT_results_MT)):
        num=0
        for j in range(len(PMT_results_MT[0])):
            if PMT_results_MT[i][j]==0:
                num=num+1
        print(num/1000)
        sheet.write(i,0,num/1000)
    print("Jaccard-VR")
    for i in range(len(PMT_results_Jaccard)):
        num = 0
        for j in range(len(PMT_results_Jaccard[0])):
            if PMT_results_Jaccard[i][j] == 0:
                num = num + 1
        print(num / 1000)
        sheet.write(i, 2, num / 1000)
    print("Wilcoxon-VR")
    for i in range(len(PMT_results_Wilcoxon)):
        num = 0
        for j in range(len(PMT_results_Wilcoxon[0])):
            if PMT_results_Wilcoxon[i][j] == 0:
                num = num + 1
        print(num / 1000)
        sheet.write(i, 1, num / 1000)
    print("Wilcoxon-F")
    for i in range(len(PMT_results_MT)):
        TP=0
        TN=0
        for j in range(len(PMT_results_MT[0])):
            if (PMT_results_MT[i][j]==0) and (PMT_results_Wilcoxon[i][j]==0):
                TP=TP+1
            elif (PMT_results_MT[i][j]==1) and (PMT_results_Wilcoxon[i][j]==1):
                TN=TN+1
        print(2*TP,"/",1000+TP-TN)
        sheet.write(i, 4, str(2*TP)+"/"+str(1000+TP-TN))
        sheet.write(i, 7, (2*TP) / (1000+TP-TN))
    print("Jaccard-F")
    for i in range(len(PMT_results_MT)):
        TP = 0
        TN = 0
        for j in range(len(PMT_results_MT[0])):
            if (PMT_results_MT[i][j] == 0) and (PMT_results_Jaccard[i][j] == 0):
                TP = TP + 1
            elif (PMT_results_MT[i][j] == 1) and (PMT_results_Jaccard[i][j] == 1):
                TN = TN + 1
        print(2 * TP, "/", 1000 + TP - TN)
        sheet.write(i, 5, str(2 * TP) + "/" + str(1000 + TP - TN))
        sheet.write(i, 8, (2 * TP) / (1000 + TP - TN))
    book.save("/mnt/c/resultstime/"+object+"/dataAnalysisTwo.xls")

def dataAnalysisThree():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    read_excel_route_H = ["/mnt/c/resultstime/"+object+"/MR-all_MT_H.xls",
                        "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_H.xls",
                        "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_H.xls"]
    read_excel_route_G = ["/mnt/c/resultstime/"+object+"/MR-all_MT_G.xls",
                          "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_G.xls",
                          "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_G.xls"]
    read_excel_route_1_PMax = ["/mnt/c/resultstime/"+object+"/MR-all_MT_PMax.xls",
                          "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_PMax.xls",
                          "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_PMax.xls"]

    for i in range(len(read_excel_route_H)):
        read_book = xlrd.open_workbook(read_excel_route_H[i])
        read_sheet = read_book.sheet_by_index(0)
        H=read_sheet.col_values(9)
        PMT=read_sheet.col_values(7)
        data1=[]
        data2=[]
        for j in range(1,len(H)):
            if int(PMT[j])==0:
                data1.append(float(H[j]))
            else:
                data2.append(float(H[j]))
        # ranksum返回双尾检验值p，除以2后用单尾检验和显著性水平0.05比，p<0.05则两概率分布差异大
        stat, p = ss.ranksums(data1, data2)
        print("H-P-Wilcoxon")
        print(stat, ":", p / 2)
        sheet.write(0,int(0+4*i),stat)
        sheet.write(0, int(1 + 4 * i), p/2)
        D, p = ss.ks_2samp(data1, data2,"less")
        print("H-K-S")
        print(D, ":", p)
        sheet.write(0, int(2 + 4 * i), D)
        sheet.write(0, int(3 + 4 * i), p)

    for i in range(len(read_excel_route_G)):
        read_book = xlrd.open_workbook(read_excel_route_G[i])
        read_sheet = read_book.sheet_by_index(0)
        G=read_sheet.col_values(10)
        PMT=read_sheet.col_values(7)
        data1=[]
        data2=[]
        for j in range(1,len(G)):
            if int(PMT[j])==0:
                data1.append(float(G[j]))
            else:
                data2.append(float(G[j]))
        # ranksum返回双尾检验值p，除以2后用单尾检验和显著性水平0.05比，p<0.05则两概率分布差异大
        stat, p = ss.ranksums(data1, data2)
        print("G-P-Wilcoxon")
        print(stat, ":", p / 2)
        sheet.write(1, int(0 + 4 * i), stat)
        sheet.write(1, int(1 + 4 * i), p / 2)
        D, p = ss.ks_2samp(data1, data2,"less")
        print("G-K-S")
        print(D, ":", p)
        sheet.write(1, int(2 + 4 * i), D)
        sheet.write(1, int(3 + 4 * i), p)
    for i in range(len(read_excel_route_1_PMax)):
        read_book = xlrd.open_workbook(read_excel_route_1_PMax[i])
        read_sheet = read_book.sheet_by_index(0)
        n_1_PMax=read_sheet.col_values(11)
        PMT=read_sheet.col_values(7)
        data1=[]
        data2=[]
        for j in range(1,len(n_1_PMax)):
            if int(PMT[j])==0:
                data1.append(float(n_1_PMax[j]))
            else:
                data2.append(float(n_1_PMax[j]))
        # ranksum返回双尾检验值p，除以2后用单尾检验和显著性水平0.05比，p<0.05则两概率分布差异大
        stat, p = ss.ranksums(data1, data2)
        print("1-PMax-P-Wilcoxon")
        print(stat, ":", p / 2)
        sheet.write(2, int(0 + 4 * i), stat)
        sheet.write(2, int(1 + 4 * i), p / 2)
        D, p = ss.ks_2samp(data1, data2,"less")
        print("1-PMax-K-S")
        print(D, ":", p)
        sheet.write(2, int(2 + 4 * i), D)
        sheet.write(2, int(3 + 4 * i), p)
    # excel日志保存
    book.save("/mnt/c/resultstime/"+object+"/dataAnalysisThree.xls")

def dataAnalysisFour():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    read_excel_route = [["/mnt/c/resultstime/"+object+"/MR1-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR1-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR2-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR3-1_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR4-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR5-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR6-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR7-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR8-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR9-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR10-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR11-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR12-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/"+object+"/MR-all_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_MT_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_MT_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_G.xls",
                         "/mnt/c/resultstime/"+object+"/MR-all_Jaccard_PMax.xls"]]
    for i in range(len(read_excel_route)):
        number=0
        for j in range(len(read_excel_route[0])):
            read_book = xlrd.open_workbook(read_excel_route[i][j])
            read_sheet = read_book.sheet_by_index(0)
            PMT=read_sheet.col_values(7)
            PMT_result=[]
            for k in range(1,len(PMT)):
                PMT_result.append(int(PMT[k]))
            #升序
            PMT_result_max=sorted(PMT_result)
            #降序
            PMT_result_min=sorted(PMT_result,reverse=True)
            n = 0
            m = 0
            TV = 0
            for k in range(len(PMT_result_max)):
                n = n + 1
                if PMT_result_max[k] == 0:
                    m = m + 1
                    TV = TV + k + 1
            APVD_max = 1 - TV / (n * m) + 1 / (2 * n)
            n = 0
            m = 0
            TV = 0
            for k in range(len(PMT_result_min)):
                n = n + 1
                if PMT_result_min[k] == 0:
                    m = m + 1
                    TV = TV + k + 1
            APVD_min = 1 - TV / (n * m) + 1 / (2 * n)
            if j % 3 == 0:
                NAPVD_random = 0
                NAPVD_random_all=[]
                for z in range(30):
                    PMT_random = np.array(PMT_result)
                    ###
                    np.random.shuffle(PMT_random)
                    ###
                    n_random=0
                    m_random=0
                    TV_random=0
                    F_measure=0#第一次检测到错误的测试用例数量
                    for k_random in range(len(PMT_random)):
                        n_random=n_random+1
                        if PMT_random[k_random]==0:
                            m_random=m_random+1
                            TV_random=TV_random+k_random+1
                            if F_measure==0:
                                F_measure=k_random+1
                    APVD_random=1-TV_random/(n_random*m_random)+1/(2*n_random)
                    temp=(APVD_random-APVD_min)/(APVD_max-APVD_min)
                    NAPVD_random_all.append(temp)
                    NAPVD_random=NAPVD_random+temp
                    sheet.write(int(15*(j/3+1)+i), z, temp)
                    ###
                    sheet.write(int(15 * (j / 3 + 1+3) + i), z, F_measure)
                    ###
                NAPVD_random=NAPVD_random/30
                print(NAPVD_random_all,end="  ")
                print(NAPVD_random,end="  ")
                sheet.write(i,number,NAPVD_random)
                number=number+1
            n=0
            m=0
            TV=0
            for k in range(len(PMT_result)):
                n=n+1
                if PMT_result[k]==0:
                    m=m+1
                    TV=TV+k+1
            APVD_TS=1-TV/(n*m)+1/(2*n)
            NAPVD=(APVD_TS-APVD_min)/(APVD_max-APVD_min)
            print(NAPVD,end="  ")
            sheet.write(i, number, NAPVD)
            number = number + 1
        print()
    # excel日志保存
    book.save("/mnt/c/resultstime/"+object+"/dataAnalysisFour.xls")

def dataAnalysisFive():
    read_excel_route = [["/mnt/c/resultstime/" + object + "/MR1-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR1-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR2-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR2-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR3-1_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR3-1_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR4-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR4-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR5-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR5-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR6-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR6-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR7-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR7-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR8-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR8-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR9-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR9-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR10-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR10-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR11-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR11-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR12-3_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR12-3_Jaccard_PMax.xls"],
                        ["/mnt/c/resultstime/" + object + "/MR-all_MT_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_MT_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_MT_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Wilcoxon_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Wilcoxon_PMax.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Jaccard_H.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Jaccard_G.xls",
                         "/mnt/c/resultstime/" + object + "/MR-all_Jaccard_PMax.xls"]]
    for i in range(len(read_excel_route)):
        for j in range(0,len(read_excel_route[0]),3):
            df_read = pd.read_excel(read_excel_route[i][j])
            df_G = df_read.sort_values(by='10-基尼杂质系数', ascending=False, axis=0)
            for k in range(len(df_G.index.values)):
                df_G.iloc[k, 5] = "G"
            df_G.to_excel(read_excel_route[i][j+1], index=False)
            df_PMax = df_read.sort_values(by='11-1-最大概率', ascending=False, axis=0)
            for k in range(len(df_PMax.index.values)):
                df_PMax.iloc[k, 5] = "PMax"
            df_PMax.to_excel(read_excel_route[i][j + 2], index=False)


if __name__ == '__main__':
    dataAnalysisTwo()
    dataAnalysisFive()
    dataAnalysisThree()
    dataAnalysisFour()
