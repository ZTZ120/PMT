import os

def replace_multiple_lines_with_one(folder_path, start_pattern, end_pattern, replacement_line):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):  # 只处理Python文件
                file_path = os.path.join(root, file_name)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # 处理文件内容，将多行替换为一行
                new_lines = []
                skip_lines = False
                for line in lines:
                    if start_pattern in line:
                        skip_lines = True
                        new_lines.append(replacement_line + '\n')  # 添加替换行
                    elif end_pattern in line and skip_lines:
                        skip_lines = False
                        continue  # 跳过这行，表示替换到这里
                    elif not skip_lines:
                        new_lines.append(line)  # 保留没有被替换的行

                # 写回修改后的内容
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)


def replace_in_files(folder_path, target_line, replacement_line):
    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):  # 只处理Python文件
                file_path = os.path.join(root, file_name)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # 替换目标行
                with open(file_path, 'w', encoding='utf-8') as file:
                    for line in lines:
                        if target_line in line:
                            line = line.replace(target_line, replacement_line)
                        file.write(line)

# 调用函数
folder_path = '/home/ztz/RQ1/VGG16/model'  # 替换成你的文件夹路径
target_line = '    model.fit(dataset, epochs=epochs)'  # 你想替换的行内容
replacement_line = '    #model.fit(dataset, epochs=epochs)'  # 替换后的新内容

replace_in_files(folder_path, target_line, replacement_line)


# 调用函数
folder_path = '/home/ztz/RQ1/VGG16/model'  # 替换成你的文件夹路径
start_pattern = "    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),"  # 多行替换开始的标记
end_pattern = "                  metrics=['accuracy'])"  # 多行替换结束的标记
replacement_line = ''  # 用一行替换多行

#replace_multiple_lines_with_one(folder_path, start_pattern, end_pattern, replacement_line)
