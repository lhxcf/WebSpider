import os
from PIL import Image
from tqdm import tqdm

# 用于将文件夹下的tif(或其他类型)照片换为png

def convert_tif_to_png_and_delete_original(folder_path):
    # 获取文件夹中的所有文件和子文件夹
    for filename in tqdm(os.listdir(folder_path)):
        # 检查文件是否以.tif或.tiff结尾（不区分大小写）
        # if filename.lower().endswith(('.tif', '.tiff')):
        if filename.lower().endswith('jpg'):
            # 构建文件的完整路径
            file_path = os.path.join(folder_path, filename)

            # 打开图像文件
            with Image.open(file_path) as img:
                # 生成新的文件名（将扩展名从.tif或.tiff改为.png）
                base, ext = os.path.splitext(filename)
                new_filename = base + '.png'
                new_file_path = os.path.join(folder_path, new_filename)

                # 保存图像为PNG格式
                img.save(new_file_path, 'PNG')
                # print(f'Converted and saved: {filename} -> {new_filename}')

                # 删除原有的.tif或.tiff文件
                os.remove(file_path)
                # print(f'Deleted original: {filename}')


# 指定要处理的文件夹路径
folder_to_convert = r'E:\郑的江山社稷\论文复现\Dataset\甲状腺结节数据集\2023Dataset7\Dataset7由1+4合成的大型甲状腺肿瘤超声图像分割数据集（分割后）\val\images'  # 替换为你的文件夹路径
convert_tif_to_png_and_delete_original(folder_to_convert)