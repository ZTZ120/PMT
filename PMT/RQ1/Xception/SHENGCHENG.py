# ...existing code...
import os
import shutil

src_dir = "/home/ztz/RQ1/Xception"
dest_dir = "/home/ztz/RQ1/Xception/model"


for i in range(66, 116):
    src = os.path.join(src_dir, f"Xception{i}.py")
    dst = os.path.join(dest_dir, f"Xception{i}.py")

    shutil.copy2(src, dst)            # 复制文件 -> 真实创建 demo{i}.py
    print("created", dst)
# ...existing code...