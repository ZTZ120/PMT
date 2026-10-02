# ...existing code...
import os
import shutil

src_dir = "/home/ztz/RQ1/InceptionV3"
dest_dir = "/home/ztz/RQ1/InceptionV3/model"


for i in range(91, 289):
    src = os.path.join(src_dir, f"InceptionV3_{i}.py")
    dst = os.path.join(dest_dir, f"InceptionV3_{i}.py")

    shutil.copy2(src, dst)            # 复制文件 -> 真实创建 demo{i}.py
    print("created", dst)
# ...existing code...