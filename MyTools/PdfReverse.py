from PyPDF2 import PdfReader, PdfWriter
import os

# 用于将给定pdf文件所有内容导致（1-100 -> 100-1）

def reverse_pdf_pages(input_file, output_file):
    # 打开 PDF 文件
    with open(input_file, 'rb') as file:
        pdf = PdfReader(file)
        num_pages = len(pdf.pages)

        # 创建一个新的 PDF 对象
        new_pdf = PdfWriter()

        # 从最后一页开始，逆序添加页面到新的 PDF 对象中
        for i in range(num_pages - 1, -1, -1):
            new_pdf.add_page(pdf.pages[i])

            # 将新的 PDF 对象写入文件
        with open(output_file, 'wb') as file2:
            new_pdf.write(file2)


# 文件夹名
folder_path = r"D:\software\微信\Downloads\WeChat Files\wxid_abu19bq3y71q22\FileStorage\File\2024-09"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    reverse_pdf_pages(file_path, filename)
