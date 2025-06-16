import cv2
from pathlib import Path

# 统一图像尺寸
IMAGE_SIZE = (96, 96)

# 要处理的两个目录
INPUT_OUTPUT_PAIRS = [
    # (输入路径, 输出路径)
    (
        Path("training/face_pretrain/data/real/face/lfw_funneled"),
        Path("training/face_pretrain/data/real/face_resized/lfw_funneled")
    ),
    (
        Path("training/face_pretrain/data/real/non_face/seg_train"),
        Path("training/face_pretrain/data/real/non_face_resized/seg_train")
    )
]

total_count = 0

for input_root, output_root in INPUT_OUTPUT_PAIRS:
    category = input_root.parts[-2]  # "face" 或 "non_face"
    print(f"\n开始处理类别: {category}")
    count = 0

    for class_dir in input_root.iterdir():
        if class_dir.is_dir():
            print(f"\n当前子文件夹: {class_dir.name}")
            save_dir = output_root / class_dir.name
            save_dir.mkdir(parents=True, exist_ok=True)

            for img_path in class_dir.glob("*.jpg"):
                img = cv2.imread(str(img_path))
                if img is not None:
                    resized = cv2.resize(img, IMAGE_SIZE)

                    save_path = save_dir / f"resized_{img_path.name}"
                    cv2.imwrite(str(save_path), resized)

                    count += 1
                    print(f"读取: {img_path.name}，原尺寸: {img.shape}，保存为: {save_path.name}")
                else:
                    print(f"读取失败: {img_path.name}")
    
    print(f"\n {category} 总处理图片数: {count}")
    total_count += count

print(f"\n 所有处理完成，总计图像数: {total_count}")
