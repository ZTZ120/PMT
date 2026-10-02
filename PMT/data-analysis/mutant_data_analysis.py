'''
依据excel测试结果文件，分析RQ1-4实验数据
'''
import random

import xlrd
import xlwt
import scipy.stats as ss
import numpy as np
import pandas as pd

object="MobileNet"
object_name="MobileNet"
#read_excel_route是所有蜕变关系测试结果excel路径的数组
def mutantDataAnalysisOne(read_excel_route,write_excel_route):
    write_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    write_sheet = write_book.add_sheet('mysheet', cell_overwrite_ok=False)
    for k in range(len(read_excel_route)):
        print("k:",k)
        for i in range(len(read_excel_route[k])):
            print("i:",i)
            for j in range(len(read_excel_route[k][i])):
                read_book = xlrd.open_workbook(read_excel_route[k][i][j])
                read_sheet = read_book.sheet_by_index(0)
                PMT=read_sheet.col_values(7)
                num=0
                for n in range(1,len(PMT)):
                    if int(PMT[n])==0:
                        num=num+1
                write_sheet.write(108*k+1+j, i+1, num)
    write_book.save(write_excel_route)

def mutantDataAnalysisTwo(read_excel_route,write_excel_route,length):
    write_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    write_sheet = write_book.add_sheet('mysheet', cell_overwrite_ok=False)
    for k in range(len(read_excel_route)):
        print("k:",k)
        for i in range(len(read_excel_route[k])):
            print("i:",i)
            read_book_0=xlrd.open_workbook(read_excel_route[k][i][0])
            read_sheet_0=read_book_0.sheet_by_index(0)
            image_name_0=read_sheet_0.col_values(6)
            PMT_0=read_sheet_0.col_values(7)
            #sort
            image_name_0 = image_name_0[1:len(image_name_0)]
            PMT_0 = PMT_0[1:len(PMT_0)]
            image_name_0_inds = np.argsort(image_name_0)
            # image_name_0_inds=image_name_0[1:len(image_name_0)].np.argsort()
            image_name_0_sort = []
            PMT_0_sort = []
            for t in range(len(image_name_0_inds)):
                image_name_0_sort.append(image_name_0[image_name_0_inds[t]])
                PMT_0_sort.append(PMT_0[image_name_0_inds[t]])
            #sort
            for j in range(1,len(read_excel_route[k][i])):
                read_book = xlrd.open_workbook(read_excel_route[k][i][j])
                read_sheet = read_book.sheet_by_index(0)
                image_name=read_sheet.col_values(6)
                PMT=read_sheet.col_values(7)
                # sort
                image_name = image_name[1:len(image_name)]
                PMT = PMT[1:len(PMT)]
                image_name_inds = np.argsort(image_name)
                # image_name_inds=image_name[1:len(image_name)].np.argsort()
                image_name_sort = []
                PMT_sort = []
                for t in range(len(image_name_inds)):
                    image_name_sort.append(image_name[image_name_inds[t]])
                    PMT_sort.append(PMT[image_name_inds[t]])
                # sort
                num=0
                PMT_sort_random=PMT_sort
                PMT_0_sort_random=PMT_0_sort
                #同步随机排序
                combined = list(zip(PMT_sort_random, PMT_0_sort_random))
                random.shuffle(combined)
                PMT_sort_random, PMT_0_sort_random= zip(*combined)
                for n in range(0,int(len(PMT_sort_random)*length/100)):
                    if int(PMT_sort_random[n])==0 and int(PMT_0_sort_random[n])==1:
                        num=num+1
                write_sheet.write(108*k+1+j, i+1, num)
    write_book.save(write_excel_route)

def mutantDataAnalysis():
    read_excel_route_MT=[]
    read_excel_route_Jaccard = []
    read_excel_route_Wilcoxon = []
    for i in range(1,13):
        read_excel_route_MT_MR=[]
        read_excel_route_Jaccard_MR = []
        read_excel_route_Wilcoxon_MR = []
        read_excel_route_MT_MR.append("/mnt/c/score/" + object + "/MR/MR" + str(i) + "-3_MT_H_" + object_name + ".xls")
        read_excel_route_Jaccard_MR.append("/mnt/c/score/" + object + "/MR/MR" + str(i) + "-3_Jaccard_H_" + object_name + ".xls")
        read_excel_route_Wilcoxon_MR.append("/mnt/c/score/" + object + "/MR/MR" + str(i) + "-3_Wilcoxon_H_" + object_name + ".xls")
        for j in range(1,106):
            read_excel_route_MT_MR.append("/mnt/c/score/"+object+"/MR/MR"+str(i)+"-3_MT_H_"+object_name+str(j)+".xls")
            read_excel_route_Jaccard_MR.append("/mnt/c/score/" + object + "/MR/MR" + str(i) + "-3_Jaccard_H_" +object_name +str(j) + ".xls")
            read_excel_route_Wilcoxon_MR.append("/mnt/c/score/" + object + "/MR/MR" + str(i) + "-3_Wilcoxon_H_" +object_name +str(j) + ".xls")
        read_excel_route_MT.append(read_excel_route_MT_MR)
        read_excel_route_Jaccard.append(read_excel_route_Jaccard_MR)
        read_excel_route_Wilcoxon.append(read_excel_route_Wilcoxon_MR)
    #1,108,187
    read_excel_route=[]
    read_excel_route.append(read_excel_route_MT)
    read_excel_route.append(read_excel_route_Jaccard)
    read_excel_route.append(read_excel_route_Wilcoxon)
    mutantDataAnalysisTwo(read_excel_route,"/mnt/c/score/"+object+"/mutant100"+"-all"+".xls",100)
    #for random_num in range(1,31):
        #for length in range(10,101,10):
            #mutantDataAnalysisTwo(read_excel_route,"/mnt/c/score/"+object+"/mutant-"+str(length)+"-all-"+str(random_num)+".xls",length)


if __name__ == '__main__':
    mutantDataAnalysis()
