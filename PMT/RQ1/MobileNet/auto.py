import os
import gpu_config



#os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --object_program \"/home/ztz/RQ1/MobileNet/model/MobileNet.py\"")
#for i in range(1,106):
    #os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --object_program \"/home/ztz/RQ1/MobileNet/model/MobileNet"+str(i)+".py\"")

for j in range(3,4):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Jaccard_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_MT_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Wilcoxon_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,106):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Jaccard_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_MT_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Wilcoxon_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

# os.system("python \"F:/program/ImageProbability/code/python/PMT4I/get_sort_source_image.py\" --image_folder_route \"F:/program/ImageProbability/code/python/MobileNet/image/test\" --sort_type H --excel_route \"F:/program/ImageProbability/resultstime/testResnet/sort_H_res.xls\" --object_program \"F:/program/ImageProbability/code/python/testResnet/res.py\"")
