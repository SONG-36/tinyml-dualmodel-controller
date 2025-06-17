import os
import sys
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# 添加模块路径（向上两层）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from training.face_pretrain.model_training.model import build_face_model

# 【第1段：加载数据】
X = np.load("training/face_pretrain/data/preprocessed/X_data.npy")
y = np.load("training/face_pretrain/data/preprocessed/y_data.npy")
print(f" 载入数据成功: X.shape = {X.shape}, y.shape = {y.shape}")

# 【第2段：划分训练、验证和测试集】
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
print(f" 数据集划分完成: 训练 {X_train.shape[0]}，验证 {X_val.shape[0]}，测试 {X_test.shape[0]}")

# 【第3段：构建并训练模型】
model = build_face_model(input_shape=(96, 96, 3))  # 二分类，无需 num_classes
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=15,
    batch_size=32
)

# 【第4段：评估模型性能】
loss, acc = model.evaluate(X_test, y_test)
print(f" 测试集准确率: {acc:.4f}")

# 【第5段：保存模型】
save_path = "training/face_pretrain/data/preprocessed/face_model.h5"
os.makedirs(os.path.dirname(save_path), exist_ok=True)
model.save(save_path)
print(f" 模型已保存至: {save_path}")
