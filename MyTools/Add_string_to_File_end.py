import os
from tqdm import tqdm


# 用于在指定文件夹下所有图片命名结尾添加指定字符串

strs = '_mask'   # 要在命名结尾添加的字符

def rename_images_in_folder(folder_path):
    # 获取文件夹中的所有文件和子文件夹
    for filename in tqdm(os.listdir(folder_path)):
        # 构建文件的完整路径
        file_path = os.path.join(folder_path, filename)

        # 检查是否是文件而不是文件夹
        if os.path.isfile(file_path):
            # 检查文件是否是图片（可以根据扩展名简单判断）
            image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif']
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                # 生成新的文件名（在原始文件名后加上"sat"）
                new_filename = filename.rsplit('.', 1)[0] + strs  # 保留原扩展名
                if '.' in filename:
                    new_filename += '.' + filename.rsplit('.', 1)[1]  # 加上原文件的扩展名
                new_file_path = os.path.join(folder_path, new_filename)

                # 重命名文件
                os.rename(file_path, new_file_path)



# 指定要处理的文件夹路径
folder_to_rename = r'C:\Users\32858\Desktop\遥感数据集\AerialImageDataset\train\gt'  # 替换为你的文件夹路径
rename_images_in_folder(folder_to_rename)