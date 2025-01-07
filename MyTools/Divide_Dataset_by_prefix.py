import os
import shutil
import random
from collections import defaultdict
from tqdm import tqdm


# 用于分割数据集（对于同一病人的数据，全部划分到同一集合中）
# 按照6:2:2划分


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_image_files(directory):
    return [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]


def get_prefix(filename):
    # 假设前缀是文件名中第一个下划线之前的部分，或者如果没有下划线，则是整个文件名（不包括扩展名）
    name, ext = os.path.splitext(filename)
    prefix = name.split('-') if '-' in name else name
    return '-'.join(prefix[0:2])


def split_images(image_files, ratios=[0.6, 0.2, 0.2]):
    # 按前缀分组图片
    prefix_dict = defaultdict(list)
    for image in image_files:
        prefix = get_prefix(image)
        prefix_dict[prefix].append(image)

    # 打乱所有前缀组的顺序，以确保随机性
    prefix_groups = list(prefix_dict.values())
    random.seed(11)
    random.shuffle(prefix_groups)

    # 计算每个目标文件夹应获得的图片数量
    total_images = sum(len(group) for group in prefix_groups)
    split_sizes = [int(ratio * total_images) for ratio in ratios]
    split_sizes[-1] += total_images - sum(split_sizes)  # 确保总数正确，处理浮点数舍入问题

    # 分配图片到目标文件夹
    splits = {'train': [], 'val': [], 'test': []}
    current_split_index = 0
    split_count = [0] * len(ratios)

    for group in tqdm(prefix_groups, desc='创建分配目录：'):
        if split_count[current_split_index] < split_sizes[current_split_index]:
            splits[list(splits.keys())[current_split_index]].extend(group)
            split_count[current_split_index] += len(group)
        else:
            # 切换到下一个目标文件夹，直到找到可以容纳当前组的文件夹
            current_split_index = (current_split_index + 1) % len(ratios)
            while split_count[current_split_index] >= split_sizes[current_split_index]:
                current_split_index = (current_split_index + 1) % len(ratios)
            splits[list(splits.keys())[current_split_index]].extend(group)
            split_count[current_split_index] += len(group)

    # 检查是否所有图片都已分配（理论上应该总是这样，但这是一个安全检查）
    assert sum(len(split) for split in splits.values()) == total_images

    return splits


def copy_images_to_splits(src_dir, dest_dirs, splits, target_dir):
    for split_name, images in tqdm(splits.items(), desc='复制文件到目标目录：'):
        dest_dir = os.path.join(target_dir, dest_dirs[split_name])
        ensure_dir(dest_dir)
        for image in images:
            shutil.copy(os.path.join(src_dir, image), os.path.join(dest_dir, image))


def main():
    devide_type = 'masks'  # 要分割的数据集类型：images/masks
    src_directory = r'E:\郑的江山社稷-backup\甲状腺结节\dataset\2023Dataset7\Dataset7由1+4合成的大型甲状腺肿瘤超声图像分割数据集\masks'   # 源文件绝对路径
    target_derectory = r'E:\郑的江山社稷-backup\甲状腺结节\dataset\2023Dataset7\Dataset7由1+4合成的大型甲状腺肿瘤超声图像分割数据集（分割后）'
    dest_directories = {'train': fr'train\{devide_type}', 'val': fr'val\{devide_type}', 'test': fr'test\{devide_type}'}

    image_files = get_image_files(src_directory)

    splits = split_images(image_files)

    copy_images_to_splits(src_directory, dest_directories, splits, target_derectory)


if __name__ == "__main__":
    main()