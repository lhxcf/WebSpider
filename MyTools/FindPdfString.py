import os
import fitz

# 用来在指定文件下所有的pdf中查找指定字符串，并返回所在位置pdf


# 定义文件夹路径
folder_path = r"C:\Users\32858\Desktop\2023-2024年度人文与管理学院学分证明"

# 查找字符
name = '刘浩雄'

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)

        # 打开PDF文件
        with fitz.open(file_path) as doc:
            # 遍历PDF中的所有页面
            for page in doc:
                # 提取页面文本内容
                text = page.get_text()

                # 查找是否存在指定字符
                if name in text:
                    # 如果存在，打印文件名
                    print(filename)
                    break
    else:
        print(f"文件名为：{filename} 的文件不是pdf文件！")
