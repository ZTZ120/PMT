import os
import gpu_config


# os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121.xls\" --object_program \"/home/ztz/RQ1/DenseNet121/model/DenseNet121.py\"")
# for i in range(1,95):
#     os.system("python \"/home/ztz/PMT4I/get_sort_source_image.py\" --image_folder_route \"/mnt/c/data/MNIST/test\" --sort_type H --excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121_"+str(i)+".xls\" --object_program \"/home/ztz/RQ1/DenseNet121/model/DenseNet121_"+str(i)+".py\"")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121.xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_Jaccard_H_DenseNet121.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    # os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121.xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_MT_H_DenseNet121.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    # os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121.xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_Wilcoxon_H_DenseNet121.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,95):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121_"+str(i)+".xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_Jaccard_H_DenseNet121_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        # os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121_"+str(i)+".xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_MT_H_DenseNet121_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        # os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/DenseNet121/sort_H_DenseNet121_"+str(i)+".xls\" --excel_route \"/mnt/c/score/DenseNet121/MR/MR"+str(j)+"-3_Wilcoxon_H_DenseNet121_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Jaccard_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_MT_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet.xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Wilcoxon_H_MobileNet.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,106):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Jaccard_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_MT_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/MobileNet/sort_H_MobileNet"+str(i)+".xls\" --excel_route \"/mnt/c/score/MobileNet/MR/MR"+str(j)+"-3_Wilcoxon_H_MobileNet"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50.xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_Jaccard_H_ResNet50.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50.xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_MT_H_ResNet50.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50.xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_Wilcoxon_H_ResNet50.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,96):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50_"+str(i)+".xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_Jaccard_H_ResNet50_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50_"+str(i)+".xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_MT_H_ResNet50_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/ResNet50/sort_H_ResNet50_"+str(i)+".xls\" --excel_route \"/mnt/c/score/ResNet50/MR/MR"+str(j)+"-3_Wilcoxon_H_ResNet50_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Jaccard_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_MT_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16.xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG16.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,95):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Jaccard_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_MT_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG16/sort_H_VGG16"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG16/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG16"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")


for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19.xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_Jaccard_H_VGG19.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19.xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_MT_H_VGG19.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19.xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG19.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,104):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19_"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_Jaccard_H_VGG19_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19_"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_MT_H_VGG19_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/VGG19/sort_H_VGG19_"+str(i)+".xls\" --excel_route \"/mnt/c/score/VGG19/MR/MR"+str(j)+"-3_Wilcoxon_H_VGG19_"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")

for j in range(1,13):
    os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Jaccard_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_MT_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception.xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Wilcoxon_H_Xception.xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    for i in range(1,116):
        os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Jaccard --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Jaccard_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type MT --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_MT_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
    #for i in range(1,92):
        #os.system("python \"/home/ztz/PMT4I/get_PMT.py\" --probabilistic_type Wilcoxon --read_excel_route \"/mnt/c/score/Xception/sort_H_Xception"+str(i)+".xls\" --excel_route \"/mnt/c/score/Xception/MR/MR"+str(j)+"-3_Wilcoxon_H_Xception"+str(i)+".xls\" --MR "+str(j)+" --param 3 --image_rows 1000")
