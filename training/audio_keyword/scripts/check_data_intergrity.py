import numpy as np
import os

# === 设置路径 ===
data_dir = "training/audio_keyword/data/preprocessed"
X_path = os.path.join(data_dir, "X.npy")
y_path = os.path.join(data_dir, "y.npy")
label_path = os.path.join(data_dir, "labels.npy")  # 如果有的话

# === 加载数据 ===
X = np.load(X_path)
y = np.load(y_path)

print("X shape:", X.shape)
print("y shape:", y.shape)

# === 检查样本数量是否一致 ===
if X.shape[0] != y.shape[0]:
    print("错误：X 和 y 的样本数量不一致！")
    exit(1)
else:
    print("样本数量一致")

# === 检查维度 ===
if len(X.shape) != 4:
    print("错误：X 应该为 4 维 (samples, 40, 101, 1)")
else:
    print("X 的维度正常:", X.shape)

# === 标签检查 ===
print("标签数量：", len(np.unique(y)))
print("标签分布：", np.bincount(y.astype(int)))

# === （可选）检查标签映射 ===
try:
    labels = np.load(label_path)
    print("标签名称样本：", labels[:5])
    if len(np.unique(y)) != len(np.unique(labels)):
        print("标签数与名称不一致，可能标签未映射")
    else:
        print("标签名称与标签数一致")
except Exception as e:
    print("无法加载标签名称（labels.npy），跳过：", e)
