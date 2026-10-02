import subprocess
import sys
import os

# 当前环境的 Python 解释器路径
python_executable = sys.executable  # 获取当前 Python 环境的解释器路径

# 存放 demo 脚本的目录路径
script_dir = "/home/ztz/RQ1/LeNet/"

# 循环执行 demo1.py 到 demo89.py
for i in range(50, 59):
    script_name = f"LeNet{i}.py"
    script_path = os.path.join(script_dir, script_name)
    print(f"正在运行 {script_name}...")
    
    # 使用 subprocess 在当前环境中运行每个脚本
    subprocess.run([python_executable, script_path])
    
print("所有 demo 已成功执行。")
