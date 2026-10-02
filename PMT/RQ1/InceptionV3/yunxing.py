import subprocess
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import gpu_config

# 当前环境的 Python 解释器路径
python_executable = sys.executable  # 获取当前 Python 环境的解释器路径

# 存放 demo 脚本的目录路径
script_dir = "/home/ztz/RQ1/InceptionV3/"

# 定义同时运行的最大任务数
max_workers = 3

def run_script(script_name):
    script_path = os.path.join(script_dir, script_name)
    print(f"正在运行 {script_name}...")
    subprocess.run([python_executable, script_path])
    print(f"{script_name} 运行完成！")

if __name__ == "__main__":
    # 生成脚本名称列表
    script_names = [f"InceptionV3_{i}.py" for i in range(1, 289)]

    # 使用线程池限制并发任务数量
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(run_script, script_names)

    print("所有脚本已成功执行。")