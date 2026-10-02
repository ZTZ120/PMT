import os
#D:\prg\anaconda3\envs\common_env\python get_sort_source_image.py --image_folder_route "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/testCNN/image/test" --sort_type H --excel_route "C:/Users/Desktop/testCNN.xls" --object_program "E:/Program Files/PyCharm Community Edition 2020.1.1/projects/testCNN/demo.py"
#D:\prg\anaconda3\envs\common_env\python get_PMT.py --probabilistic_type Jaccard --read_excel_route "C:/Users/Desktop/testCNN.xls" --excel_route "C:/Users/Desktop/testCNNresult.xls" --MR 2 --param 3

# os.system("python \"D:\\PMT4I\\get_sort_source_image.py\" --image_folder_route \"F:/program/ImageProbability/code/python/testCNN/image/test\" --sort_type H --excel_route \"F:/program/ImageProbability/resultstime/testCNN/sort_H_demo.xls\" --object_program \"F:/program/ImageProbability/code/python/testCNN/demo.py\"")
# os.system("python \"F:/program/ImageProbability/code/python/PMT4I/get_sort_source_image.py\" --image_folder_route \"F:/program/ImageProbability/code/python/testCNN/image/test\" --sort_type H --excel_route \"F:/program/ImageProbability/code/python/testCNN/sort_H_demo1.xls\" --object_program \"F:/program/ImageProbability/code/python/testCNN/demo1.py\"")

#os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/image/test\" --sort_type H --excel_route \"/mnt/c/score/Alexnet/sort_H_demo.xls\" --object_program \"/home/ztz/RQ1/testCNN/model/demo.py\"")
#for i in range(1,90):
    #os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/image/test\" --sort_type H --excel_route \"/mnt/c/score/Alexnet/sort_H_demo"+str(i)+".xls\" --object_program \"/home/ztz/RQ1/testCNN/model/demo"+str(i)+".py\"")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo.xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_Jaccard_H_demo.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo.xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_MT_H_demo.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo.xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_Wilcoxon_H_demo.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,90):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo"+str(i)+".xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_Jaccard_H_demo"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo"+str(i)+".xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_MT_H_demo"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Alexnet/sort_H_demo"+str(i)+".xls\" --excel_route \"/mnt/c/score/Alexnet/MR/MR"+str(j)+"-3_Wilcoxon_H_demo"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

# os.system("python \"F:/program/ImageProbability/code/python/PMT4I/get_sort_source_image.py\" --image_folder_route \"F:/program/ImageProbability/code/python/testCNN/image/test\" --sort_type H --excel_route \"F:/program/ImageProbability/resultstime/testResnet/sort_H_res.xls\" --object_program \"F:/program/ImageProbability/code/python/testResnet/res.py\"")
