import tensorflow as tf
from tensorflow.keras import layers, models

def build_face_model(input_shape=(96, 96, 3)) -> tf.keras.Model:
    model = models.Sequential([

        # 第 1 层：Conv2D，提取边缘等低级特征，输出通道数为 8
        layers.Conv2D(8, kernel_size=(3, 3), strides=1, activation='relu', input_shape=input_shape),
        
        # 第 2 层：MaxPooling2D，空间下采样，减小尺寸 96x96 → 47x47
        layers.MaxPooling2D(pool_size=(2, 2)),

        # 第 3 层：Conv2D，提取更复杂的纹理特征，输出通道数 16
        layers.Conv2D(16, kernel_size=(3, 3), strides=1, activation='relu'),
        
        # 第 4 层：再次下采样，尺寸变为 22x22
        layers.MaxPooling2D(pool_size=(2, 2)),

        # 第 5 层：Conv2D，提取更深层次的语义信息，输出通道数 32
        layers.Conv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
        
        # 第 6 层：下采样到 10x10
        layers.MaxPooling2D(pool_size=(2, 2)),

        # 第 7 层：Flatten，将特征图展平为一维向量（3200维）
        layers.Flatten(),

        # 第 8 层：Dense 全连接层，64 个神经元，进一步抽象特征
        layers.Dense(64, activation='relu'),

        # 第 9 层：输出层，1 个神经元，sigmoid 激活用于二分类（人脸 / 非人脸）
        layers.Dense(1, activation='sigmoid')
    ])

    return model
