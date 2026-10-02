import os
import gpu_config
os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --object_program \"/home/ztz/RQ1/VGG16/model/VGG16.py\"")
for i in range(1,95):
    os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --object_program \"/home/ztz/RQ1/VGG16/model/VGG16_"+str(i)+".py\"")

for j in range(1,13):
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Jaccard_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_MT_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,95):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Jaccard_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_MT_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

# os.system("python \"F:/program/ImageProbability/code/python/PMT4I/get_sort_source_image.py\" --image_folder_route \"F:/program/ImageProbability/code/python/VGG16/image/test\" --sort_type H --excel_route \"F:/program/ImageProbability/resultstime/testResnet/sort_H_res.xls\" --object_program \"F:/program/ImageProbability/code/python/testResnet/res.py\"")
