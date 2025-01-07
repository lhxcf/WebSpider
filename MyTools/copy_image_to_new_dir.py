import os
import shutil
from tqdm import tqdm

def copy_images(image_names_file, source_dir, destination_dir):
    # 检查源文件夹是否存在
    if not os.path.exists(source_dir):
        print(f"源文件夹 {source_dir} 不存在！")
        return

    # 创建目标文件夹（如果不存在）
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # 读取包含图片名称的txt文件
    try:
        with open(image_names_file, 'r', encoding='utf-8') as file:
            image_names = file.readlines()
    except FileNotFoundError:
        print(f"文件 {image_names_file} 不存在！")
        return

    # 去除每行末尾的换行符
    image_names = [name.strip() for name in image_names]

    # 复制图片
    for name in tqdm(image_names):
        source_path = os.path.join(source_dir, name)
        destination_path = os.path.join(destination_dir, name)

        # 检查文件是否存在
        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            print(f"已复制: {name}")
        else:
            print(f"文件 {name} 不存在于源文件夹中！")

# 示例用法
image_names_file = r'E:\郑的江山社稷-backup\论文复现\FCtL-main\txt_1\train.txt'  # 包含图片名称的txt文件
source_dir = r'E:\郑的江山社稷-backup\论文复现\FCtL-main\data_1\train\Sat'  # 源文件夹
destination_dir = r'E:\郑的江山社稷-backup\论文复现\FCtL-main\data_1\crossvali'  # 目标文件夹

copy_images(image_names_file, source_dir, destination_dir)