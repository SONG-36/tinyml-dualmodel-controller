import kagglehub
from pathlib import Path
import shutil
import zipfile
import os

def extract_zip_files(folder: Path, target_dir: Path):
    for zip_path in folder.glob("*.zip"):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        print(f" 解压完成: {zip_path.name}")
        zip_path.unlink()  # 删除 zip 文件


def download_and_move(kaggle_slug: str, subfolder: str, dataset_name: str):
    print(f"\n 正在下载 '{dataset_name}' 数据集...")
    dataset_path = kagglehub.dataset_download(kaggle_slug)
    raw_path = Path(dataset_path)
    print(" 原始下载路径:", raw_path)

    # 创建目标目录
    target_dir = Path("training/face_pretrain/data/real") / subfolder
    target_dir.mkdir(parents=True, exist_ok=True)

    # 解压 zip 文件（如果有）
    extract_zip_files(raw_path, target_dir)

    # 遍历目录下所有内容并移动（非 zip）
    for item in raw_path.iterdir():
        if item.suffix != ".zip":
            shutil.move(str(item), str(target_dir / item.name))

    print(f" 已移动到: {target_dir}")

    # 删除空的下载目录
    try:
        raw_path.rmdir()
    except OSError:
        pass  # 如果还有子文件夹未被移除，不报错


if __name__ == "__main__":
    # 下载人脸图像（LFW People）
    download_and_move(
        kaggle_slug="atulanandjha/lfwpeople",
        subfolder="face",
        dataset_name="LFW Face Dataset"
    )

    # 下载非人脸图像（Intel Classification）
    download_and_move(
        kaggle_slug="puneet6060/intel-image-classification",
        subfolder="non_face",
        dataset_name="Intel Image Classification"
    )
