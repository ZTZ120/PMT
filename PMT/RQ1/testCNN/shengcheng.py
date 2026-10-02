# ...existing code...
import os
import shutil

src_dir = "/home/ztz/RQ1/testCNN"
dest_dir = "/home/ztz/RQ1/testCNN/model"


for i in range(1, 90):
    src = os.path.join(src_dir, f"demo{i}.py")
    dst = os.path.join(dest_dir, f"demo{i}.py")

    shutil.copy2(src, dst)            # 复制文件 -> 真实创建 demo{i}.py
    print("created", dst)
# ...existing code...