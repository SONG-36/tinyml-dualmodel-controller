import cv2
from pathlib import Path

# 统一图像尺寸
IMAGE_SIZE = (96, 96)

# 要处理的多个目录
INPUT_OUTPUT_PAIRS = [
    # 人脸图像
    # (
    #     Path("training/face_pretrain/data/real/face/lfw_funneled"),
    #     Path("training/face_pretrain/data/real/face_resized/lfw_funneled")
    # ),

    # 非人脸图像：train/test/pred 三个子目录
    # (
    #     Path("training/face_pretrain/data/real/non_face/seg_train"),
    #     Path("training/face_pretrain/data/real/non_face_resized/seg_train")
    # ),
    # (
    #     Path("training/face_pretrain/data/real/non_face/seg_test"),
    #     Path("training/face_pretrain/data/real/non_face_resized/seg_test")
    # ),
    (
        Path("training/face_pretrain/data/real/non_face/seg_pred"),
        Path("training/face_pretrain/data/real/non_face_resized/seg_pred")
    ),
]

total_count = 0

for input_root, output_root in INPUT_OUTPUT_PAIRS:
    category = input_root.parts[-2]
    print(f"\n开始处理类别: {category}")
    count = 0

    for path in input_root.iterdir():
        if path.is_dir():
            # 子文件夹（如 lfw_funneled/Aaron_xxx）
            print(f"\n当前子文件夹: {path.name}")
            save_dir = output_root / path.name
            save_dir.mkdir(parents=True, exist_ok=True)

            for img_path in path.glob("*.jpg"):
                img = cv2.imread(str(img_path))
                if img is not None:
                    resized = cv2.resize(img, IMAGE_SIZE)
                    save_path = save_dir / f"resized_{img_path.name}"
                    cv2.imwrite(str(save_path), resized)
                    count += 1
                    print(f" 读取: {img_path.name}, 原尺寸: {img.shape}, 保存为: {save_path.name}")
        elif path.suffix.lower() == ".jpg":
            # 🖼 直接是图片文件（如 seg_pred/*.jpg）
            output_root.mkdir(parents=True, exist_ok=True)
            img = cv2.imread(str(path))
            if img is not None:
                resized = cv2.resize(img, IMAGE_SIZE)
                save_path = output_root / f"resized_{path.name}"
                cv2.imwrite(str(save_path), resized)
                count += 1
                print(f"✅ 读取: {path.name}, 原尺寸: {img.shape}, 保存为: {save_path.name}")
            else:
                print(f"⚠️ 无法读取图片: {path.name}")

    print(f"\n📦 类别 {category} 处理完毕，总图像数: {count}")
    total_count += count


print(f"\n 所有处理完成，总计图像数: {total_count}")
