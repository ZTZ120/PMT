# gpu_config.py
import tensorflow as tf

def set_gpu_memory_growth():
    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            print(f"✅ 已启用按需分配显存，物理GPU数量：{len(gpus)}")
        except RuntimeError as e:
            print(f"❌ 启用按需分配显存失败：{e}")

# 导入时自动执行配置（无需主脚本调用）
set_gpu_memory_growth()