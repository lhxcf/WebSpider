import os
from PIL import Image
from tqdm import tqdm


# 用于将指定文件中所有的PNG文件转为JPG文件

def convert_png_to_jpg(input_folder):
    # 遍历文件夹中的所有文件
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    if not png_files:
        print("No PNG files found in the specified folder.")
        return

    # 使用tqdm创建进度条
    for filename in tqdm(png_files, desc="Converting PNG to JPG", unit="file"):
        # 构建完整的文件路径
        input_path = os.path.join(input_folder, filename)
        # 构建输出文件的路径，将扩展名改为.jpg
        output_path = os.path.join(input_folder, os.path.splitext(filename)[0] + '.jpg')

        try:
            # 打开PNG图片
            with Image.open(input_path) as img:
                # 将图片转换为RGB模式（如果图片是RGBA模式，则去掉alpha通道）
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                # 保存为JPG格式
                img.save(output_path, 'JPEG')
                # 删除原始的PNG文件
                os.remove(input_path)
        except Exception as e:
            print(f"Failed to convert {input_path}. Error: {e}")

    print("All files have been processed.")


# 指定文件夹路径
folder_path = r'E:\郑的江山社稷-backup\甲状腺结节\dataset\VOCdevkit\VOC2007\JPEGImages'  # 替换为你的文件夹路径
convert_png_to_jpg(folder_path)