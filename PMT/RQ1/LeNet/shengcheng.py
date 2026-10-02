# ...existing code...
import os
import shutil

src_dir = "/home/ztz/RQ1/LeNet"
dest_dir = "/home/ztz/RQ1/LeNet/model"


for i in range(1, 70):
    src = os.path.join(src_dir, f"LeNet{i}.py")
    dst = os.path.join(dest_dir, f"LeNet{i}.py")

    shutil.copy2(src, dst)            # 复制文件 -> 真实创建 demo{i}.py
    print("created", dst)
# ...existing code...