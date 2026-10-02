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
folder_path = '/home/ztz/RQ1/EfficientNet'  # 替换成你的文件夹路径
target_line = '    epochs=5'  # 你想替换的行内容
replacement_line = '    epochs=5'  # 替换后的新内容

replace_in_files(folder_path, target_line, replacement_line)


# 调用函数
folder_path = '/home/ztz/RQ1/EfficientNet/model'  # 替换成你的文件夹路径
start_pattern = "if __name__ == '__main__':"  # 多行替换开始的标记
end_pattern = "    print(result)"  # 多行替换结束的标记
replacement_line = ''  # 用一行替换多行

#replace_multiple_lines_with_one(folder_path, start_pattern, end_pattern, replacement_line)
def insert_lines_between_markers(folder_path, start_pattern, end_pattern, insert_lines, keep_markers=True, first_only=False):
    """
    在每个 .py 文件中，找到 start_pattern 和 end_pattern 之间的位置，
    在两者之间插入多行代码 insert_lines（list 或 单个字符串）。
    参数:
      - folder_path: 要处理的目录
      - start_pattern: 起始标记（包含该行）
      - end_pattern: 结束标记（包含该行）
      - insert_lines: 要插入的行（字符串或字符串列表），不需要包含换行符
      - keep_markers: 是否保留 start/end 标记行（默认 True）
      - first_only: 每个文件只修改第一个匹配区间（默认 False，修改所有区间）
    """
    if isinstance(insert_lines, str):
        insert_lines = [insert_lines]
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if not file_name.endswith('.py'):
                continue
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            new_lines = []
            i = 0
            modified = False
            while i < len(lines):
                line = lines[i]
                if start_pattern in line:
                    # 保留或删除起始行
                    if keep_markers:
                        new_lines.append(line)
                    # 将插入行添加进来
                    for ins in insert_lines:
                        new_lines.append(ins.rstrip('\n') + '\n')
                    i += 1
                    # 复制直到遇到结束标记（包含结束标记）
                    while i < len(lines):
                        if end_pattern in lines[i]:
                            if keep_markers:
                                new_lines.append(lines[i])
                            i += 1
                            break
                        else:
                            # 如果保留中间原行，也加入，否则跳过中间原行
                            if keep_markers:
                                new_lines.append(lines[i])
                            i += 1
                    modified = True
                    if first_only:
                        # 将剩余部分直接接上
                        new_lines.extend(lines[i:])
                        break
                else:
                    new_lines.append(line)
                    i += 1

            if modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)

#示例用法（取消注释以执行）
# insert_lines_between_markers(
#     folder_path='/home/ztz/RQ1/EfficientNet/model',
#     start_pattern="    model.load_weights(weights_path)",
#     end_pattern="    # 处理测试图片路径列表",
#     insert_lines=[
#         "    for layer in model.layers:",
#         "        if isinstance(layer, tf.keras.layers.BatchNormalization):",
#         "            layer.trainable = False"
#     ],
#     keep_markers=True,
#     first_only=True
# )
