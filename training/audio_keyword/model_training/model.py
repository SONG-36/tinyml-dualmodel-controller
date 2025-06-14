import tensorflow as tf

# 构建模型：输入特征为 Log-Mel（尺寸 [40, 101, 1]）
def build_model(input_shape=(40, 101, 1), num_classes=10):
    model = tf.keras.models.Sequential([
        # 第1层：二维卷积层，提取局部空间特征
        # 输出特征图尺寸： (40 - 3 + 1) × (101 - 3 + 1) × 8 = 38 × 99 × 8
        tf.keras.layers.Conv2D(filters=8, kernel_size=(3, 3), activation='relu', input_shape=input_shape),

        # 第2层：最大池化层，降低空间分辨率
        # 输出尺寸：38/2 × 99/2 × 8 ≈ 19 × 49 × 8
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # 第3层：第二个卷积层，增加通道深度提取更复杂特征
        # 输出： (19 - 3 + 1) × (49 - 3 + 1) × 16 = 17 × 47 × 16
        tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),

        # 第4层：再次池化，压缩特征图尺寸
        # 输出：17/2 × 47/2 × 16 ≈ 8 × 23 × 16
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # 第5层：展平层，准备输入全连接层
        # 输出维度：8 × 23 × 16 = 2944
        tf.keras.layers.Flatten(),

        # 第6层：全连接隐藏层，压缩特征维度
        tf.keras.layers.Dense(units=32, activation='relu'),

        # 第7层：输出层，softmax 分类为 num_classes 个类别
        tf.keras.layers.Dense(units=num_classes, activation='softmax')
    ])

    return model
