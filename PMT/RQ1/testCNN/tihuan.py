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

def replace_multiple_lines_with_multiple(folder_path, start_pattern, end_pattern, replacement_lines):
    """多行替换为多行"""
    """
    Args:
        folder_path: 文件夹路径
        start_pattern: 开始匹配模式
        end_pattern: 结束匹配模式
        replacement_lines: 替换的多行内容（列表形式，每个元素为一行）
    """
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.py'):  # 只处理Python文件
                file_path = os.path.join(root, file_name)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                # 处理文件内容，多行替换为多行
                new_lines = []
                skip_lines = False
                for line in lines:
                    if start_pattern in line:
                        skip_lines = True
                        # 添加多行替换内容（每行加上换行符）
                        for rep_line in replacement_lines:
                            new_lines.append(rep_line + '\n')
                    elif end_pattern in line and skip_lines:
                        skip_lines = False
                        continue  # 跳过结束行
                    elif not skip_lines:
                        new_lines.append(line)  # 保留未被替换的行

                # 写回修改后的内容
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(new_lines)
# 调用函数
folder_path = '/home/ztz/RQ1/testCNN'  # 替换成你的文件夹路径
target_line = ''  # 你想替换的行内容
replacement_line = ''   # 替换后的新内容

replace_in_files(folder_path, target_line, replacement_line)


# 调用函数
folder_path = '/home/ztz/RQ1/testCNN/model'  # 替换成你的文件夹路径
start_pattern = "    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),"  # 多行替换开始的标记
end_pattern = "                  loss='categorical_crossentropy', metrics=['accuracy'])"  # 多行替换结束的标记
replacement_line = ''  # 用一行替换多行

#replace_multiple_lines_with_one(folder_path, start_pattern, end_pattern, replacement_line)
# 2. 多行替换为单行示例
folder_path_model = '/home/ztz/RQ1/testCNN/model'
start_pattern = "tf.disable_v2_behavior()"  # 多行替换开始的标记
end_pattern = "def testAPI(teststr):"  # 多行替换结束的标记


# 3. 多行替换为多行示例
replacement_multi_lines = [
    'tf.disable_v2_behavior()',
    'def testAPI(teststr):',
]
#replace_multiple_lines_with_multiple(folder_path_model, start_pattern, end_pattern, replacement_multi_lines)
