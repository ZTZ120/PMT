import os
import gpu_config


os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --object_program \"/home/ztz/RQ1/Xception/model/Xception.py\"")
for i in range(1,116):
    os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --object_program \"/home/ztz/RQ1/Xception/model/Xception"+str(i)+".py\"")

for j in range(1,13):
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Jaccard_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_MT_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Wilcoxon_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,116):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Jaccard_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_MT_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Wilcoxon_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
