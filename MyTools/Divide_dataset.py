import os
import shutil
import random
from tqdm import tqdm


# **随机** 分割数据集，按6:2:2划分

# 调用函数，指定dir文件夹路径
dir_path = r'E:\郑的江山社稷-backup\甲状腺结节\dataset\2023Dataset7\Dataset7由1+4合成的大型甲状腺肿瘤超声图像分割数据集\images'  # 替换为你的图片文件夹路径
target_path = r'E:\郑的江山社稷-backup\甲状腺结节\dataset\2023Dataset7\Dataset7由1+4合成的大型甲状腺肿瘤超声图像分割数据集（分割后）'    # 分割后文件路径夹


def split_images(dir_path, train_ratio=0.6, val_ratio=0.2, test_ratio=0.2):
    # 确保总比例为1
    assert train_ratio + val_ratio + test_ratio == 1.0, "The sum of ratios must be 1.0"

    # 获取dir文件夹下的所有图片文件
    image_files = [f for f in tqdm(os.listdir(dir_path), desc='Load files_path:') if f.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
    random.seed(11)
    # 打乱图片文件列表
    random.shuffle(image_files)

    # 计算每个文件夹应包含的图片数量
    total_images = len(image_files)
    train_count = int(total_images * train_ratio)
    val_count = int(total_images * val_ratio)
    test_count = total_images - train_count - val_count  # 剩下的都是test

    # 创建目标文件夹
    train_dir = os.path.join(target_path, 'train')
    val_dir = os.path.join(target_path, 'val')
    test_dir = os.path.join(target_path, 'test')

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # 分配图片到各个文件夹
    train_files = image_files[:train_count]
    val_files = image_files[train_count:train_count + val_count]
    test_files = image_files[train_count + val_count:]

    for file in tqdm(train_files, desc='Divide train_files:'):
        shutil.copy(os.path.join(dir_path, file), os.path.join(train_dir, file))

    for file in tqdm(val_files, desc='Divide val_files:'):
        shutil.copy(os.path.join(dir_path, file), os.path.join(val_dir, file))

    for file in tqdm(test_files, desc='Divide test_files:'):
        shutil.copy(os.path.join(dir_path, file), os.path.join(test_dir, file))

    print(f"Images have been split into train ({train_count}), val ({val_count}), and test ({test_count}) folders.")


split_images(dir_path)
