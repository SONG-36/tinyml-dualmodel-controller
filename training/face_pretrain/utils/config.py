# training/face_pretrain/utils/config.py

import os

# 获取项目根路径（向上两层）
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 原始图像路径
FACE_DIR = os.path.join(PROJECT_ROOT, "training", "face_pretrain", "data", "real", "face", "lfw_funneled")
NON_FACE_DIR = os.path.join(PROJECT_ROOT, "training", "face_pretrain", "data", "real", "non_face", "seg_train")

# 预处理输出路径
PREPROCESS_DIR = os.path.join(PROJECT_ROOT, "data", "preprocessed")
X_PATH = os.path.join(PREPROCESS_DIR, "X_face.npy")
Y_PATH = os.path.join(PREPROCESS_DIR, "y_face.npy")

# 图像尺寸
IMAGE_SIZE = (96, 96)

# 模型训练保存路径
MODEL_DIR = os.path.join(PROJECT_ROOT, "training", "face_pretrain", "model_training")
H5_MODEL_PATH = os.path.join(MODEL_DIR, "face_model.h5")

# 量化导出路径
EXPORT_DIR = os.path.join(PROJECT_ROOT, "training", "face_pretrain", "export_model")
TFLITE_MODEL_PATH = os.path.join(EXPORT_DIR, "face_model_int8.tflite")

# 推理测试路径（benchmark 用）
BENCHMARK_DIR = os.path.join(PROJECT_ROOT, "training", "face_pretrain", "benchmark")

# 创建目录（若不存在）
for path in [PREPROCESS_DIR, EXPORT_DIR, BENCHMARK_DIR]:
    os.makedirs(path, exist_ok=True)
