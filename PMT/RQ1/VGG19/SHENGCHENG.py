# ...existing code...
import os
import shutil

src_dir = "/home/ztz/RQ1/VGG19"
dest_dir = "/home/ztz/RQ1/VGG19/model"


for i in range(1, 104):
    src = os.path.join(src_dir, f"VGG19_{i}.py")
    dst = os.path.join(dest_dir, f"VGG19_{i}.py")

    shutil.copy2(src, dst)            # 复制文件 -> 真实创建 demo{i}.py
    print("created", dst)
# ...existing code...