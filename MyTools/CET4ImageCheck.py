import os
from PIL import Image

# 用于检查给定文件夹下的照片是否符合CET4的要求（不检查图片背景）


def check_photos(folder_path):
    # 获取文件夹中所有文件
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)

        # 检查文件是否为jpg格式
        if not file.endswith('.jpg'):
            # 将非jpg格式的图片转换为jpg格式
            convert_to_jpg(file_path.lower())

        # 检查照片大小和内存占用
        image = Image.open(file_path)
        image_size = image.size
        image_memory = os.path.getsize(file_path) / 1024  # 将文件大小转换为KB

        # 检查照片大小是否在指定范围内
        if not (192 <= image_size[1] <= 320 and 144 <= image_size[0] <= 240):
            # 调整照片大小为指定范围
            resize_image(file_path)
        # 检查照片占用内存是否在指定范围内
        if not (20 <= image_memory <= 50):
            # 压缩照片质量以减小文件大小
            compress_image(file_path)
        print(f"完成照片/{file_path[-22:]}")


def convert_to_jpg(file_path):
    image = Image.open(file_path)
    new_file_path = os.path.splitext(file_path)[0] + '.jpg'
    image.save(new_file_path, 'JPEG')
    os.remove(file_path)


def resize_image(file_path):
    image = Image.open(file_path)
    new_image = image.resize((240, 320))
    new_image.save(file_path)


def compress_image(file_path):
    image = Image.open(file_path)
    image.save(file_path, optimize=True, quality=100)


# 指定照片文件夹路径
folder_path = r"C:\Users\32858\Desktop\照片"
check_photos(folder_path)