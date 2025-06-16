import tensorflow as tf
import numpy as np
import os

# 加载模型
model = tf.keras.models.load_model("training/audio_keyword/data/preprocessed/keyword_model.h5")

# 设置转换器
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]

# 设置代表性数据集
X = np.load("training/audio_keyword/data/preprocessed/X.npy")
if X.ndim == 3:
    X = np.expand_dims(X, axis=-1)  # 添加通道维度

def representative_dataset():
    for i in range(100):
        yield [X[i:i+1].astype(np.float32)]

converter.representative_dataset = representative_dataset
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

# 转换模型
tflite_model = converter.convert()

# 保存模型
os.makedirs("export_model", exist_ok=True)
tflite_path = "training/audio_keyword/export_model/keyword_model_int8.tflite"
with open(tflite_path, "wb") as f:
    f.write(tflite_model)

print(f"模型已导出: {tflite_path}")
print(f"大小: {os.path.getsize(tflite_path) / 1024:.2f} KB")
