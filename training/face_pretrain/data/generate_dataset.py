import cv2
import numpy as np
from pathlib import Path
import os

# 参数配置
IMAGE_SIZE = (96, 96)

# 输入目录
FACE_DIR = Path("training/face_pretrain/data/real/face_resized/lfw_funneled")
NON_FACE_ROOT = Path("training/face_pretrain/data/real/non_face_resized")
NON_FACE_SUBDIRS = ["seg_train", "seg_test", "seg_pred"]

# 输出文件路径
OUTPUT_X = Path("training/face_pretrain/data/preprocessed/X_data.npy")
OUTPUT_Y = Path("training/face_pretrain/data/preprocessed/y_data.npy")

def load_images_from_folder(folder: Path, label: int, recursive: bool = True):
    images = []
    labels = []
    if recursive:
        for subfolder in folder.iterdir():
            if subfolder.is_dir():
                for img_path in subfolder.glob("*.jpg"):
                    img = cv2.imread(str(img_path))
                    if img is not None:
                        resized = cv2.resize(img, IMAGE_SIZE)
                        normalized = resized.astype(np.float32) / 255.0
                        images.append(normalized)
                        labels.append(label)
    else:
        for img_path in folder.glob("*.jpg"):
            img = cv2.imread(str(img_path))
            if img is not None:
                resized = cv2.resize(img, IMAGE_SIZE)
                normalized = resized.astype(np.float32) / 255.0
                images.append(normalized)
                labels.append(label)
    return images, labels

def main():
    print("🧠 正在读取人脸图像 ...")
    face_images, face_labels = load_images_from_folder(FACE_DIR, label=1, recursive=True)
    print(f"读取人脸图像数量: {len(face_images)}")

    print("🔍 正在读取非人脸图像 ...")
    non_face_images, non_face_labels = [], []
    for subdir in NON_FACE_SUBDIRS:
        sub_path = NON_FACE_ROOT / subdir
        print(f"📂 处理非人脸子目录: {subdir}")
        imgs, lbls = load_images_from_folder(sub_path, label=0, recursive=False)
        non_face_images.extend(imgs)
        non_face_labels.extend(lbls)
    print(f"读取非人脸图像数量: {len(non_face_images)}")

    # 拼接数据
    X = np.array(face_images + non_face_images)
    y = np.array(face_labels + non_face_labels)

    print(f"\n✅ 最终图像数量: {X.shape[0]}，图像形状: {X.shape[1:]}")
    print(f"✅ 标签数量: {y.shape[0]}，标签种类: {np.unique(y)}")

    # 保存
    np.save(OUTPUT_X, X)
    np.save(OUTPUT_Y, y)
    print(f"\n📁 数据保存成功到：\n  - {OUTPUT_X}\n  - {OUTPUT_Y}")

if __name__ == "__main__":
    main()
