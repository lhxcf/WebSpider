import tkinter
from tkinter import messagebox
import QQGroup
from AddQQGroup.SettingTools import SettingTools
import multiprocessing
from openpyxl import load_workbook
from tkinter import *


def open_setting_file():
    """
    打开配置文件
    :return:
    """
    SettingTools.open_setting_file(file_path=file_path)


def close_window():
    """
    关闭程序进程
    :return:
    """
    is_close = messagebox.askyesno('(扭曲...)爬行。。。', '真的要关闭程序了吗？？？你好狠的心哦！')
    if is_close:
        root.destroy()
    else:
        return


class MenuPage:
    """
    菜单界面
    """
    def __init__(self, master):
        self.root = tkinter.Frame(master)
        self.root.pack()
        self.menu_page()

    # 程序界面
    def menu_page(self):
        def load():
            """
            软件启动时加载
            :return:
            """
            text_list.insert(END, "正在加载配置信息...")
            global qq_path
            global is_execute
            # 检查配置文件
            is_exit = QQGroup.check_setting_exit(file_path)
            if not is_exit:
                root.quit()
            # 检查qq快捷方式的绝对路径
            message = SettingTools.check_qq_path(file_path)
            if message is not None:
                messagebox.showerror(title='错误', message=message)
                root.quit()
            # 从配置文件加载QQ路径
            workbook = load_workbook(file_path)
            qq_path = workbook['Sheet2']['A2'].value
            is_execute = workbook['Sheet2']['B2'].value
            text_list.insert(END, f"配置文件加载完成！")
            text_list.insert(END, f"QQ路径：{qq_path}")
            text_list.insert(END, f'是否启动后直接执行：{is_execute}')
            if str(is_execute).strip() == '是':
                text_list.insert(END, "正在执行QQ加群脚本...")
                add_qq_group_now()
                root.quit()

        def add_qq_group_now():
            """
            加QQ群，直接加，不弹窗
            :return:
            """
            # 启动加群程序后隐藏窗口
            root.withdraw()

            # 加群
            QQGroup.add_qq_group(qq_path, file_path)
            btn_stop.config(state=tkinter.NORMAL)
            root.quit()

        def add_qq_group():
            """
            加QQ群
            :return:
            """
            # 启动加群程序后隐藏窗口
            messagebox.showinfo("对面的呆子看过来~", "崽子~我要隐藏喽~想管我就去任务管理器去~哼~我走噜~")
            root.withdraw()

            # 加群
            QQGroup.add_qq_group(qq_path, file_path)
            btn_stop.config(state=tkinter.NORMAL)
            root.quit()

        def mul_add_qq_group():
            """
            后台运行add_qq_group，即后台运行添加QQ群进程
            :return:
            """
            global p
            p = multiprocessing.Process(target=add_qq_group)
            p.start()
            p.join()

        def kill_process():
            """
            关闭后台进程
            :return:
            """
            global p
            is_kill = messagebox.askyesno('小小的内心里有大大的疑惑！？', '确定关闭自动加群服务吗？真的吗？？？')
            if is_kill:
                p.terminate()
                messagebox.showinfo("嗯哼~", "进程已经关闭啦~")
            else:
                return

        root.title('QQ加群自动化工具')
        root.geometry("850x800+400+200")
        # 左上标签
        lab_status = Label(self.root, text="状态信息:", font=('楷体', 15))
        lab_status.grid(row=0, column=0, sticky="nsw")
        # 配置按钮
        btn_setting = Button(self.root, text='配置', font=('楷体', 15), command=open_setting_file)
        btn_setting.grid(row=0, column=1, sticky="e")

        # 列表框
        text_list = Listbox(self.root, font=('楷体', 16), width=50, height=15)
        text_list.grid(row=2, columnspan=2)

        # 开始按钮
        btn_stat = Button(self.root, text='开始', font=('楷体', 15), command=add_qq_group)
        btn_stat.grid(row=3, column=0, sticky="e")

        # 停止按钮
        btn_stop = Button(self.root, text='停止', font=('楷体', 15), command=kill_process)
        btn_stop.grid(row=3, column=1, sticky="w")
        btn_stop.config(state=tkinter.DISABLED)

        # 退出程序按钮
        btn_exit = Button(self.root, text='退出程序', font=('楷体', 15), command=close_window)
        btn_exit.grid(row=3, column=1, sticky="e")

        # 窗体打开后加载
        load()


class LogPage:
    """
    登陆界面
    """
    def __init__(self, master):
        self.root = tkinter.Frame(master)
        self.root.pack()
        self.load()

    def load(self):
        """
        显示界面时加载
        :return:
        """

        root.title('emmm登陆不了了吧嘎嘎嘎~想要检验码就联系作者哦~')

        # 设置窗口大小以及出现的位置
        root.geometry('500x100+400+200')

        # 点击右上角关闭按钮事件
        root.protocol("WM_DELETE_WINDOW", close_window)

        # 左上标签
        lab_test = Label(self.root, text="校验码：", font=('楷体', 15))
        lab_test.grid(row=1, column=0, sticky=N + S + E + W)

        # 校验码文本框
        txt_passwd = Entry(self.root, show='*', width=30)
        txt_passwd.grid(row=1, column=1, sticky="e")

        # 登陆按钮
        btn_log = Button(self.root, text='登陆', font=('楷体', 15), command=self.jump)
        btn_log.grid(row=2, column=1, sticky=W)

        # 配置窗口布局的行列数
        root.grid_rowconfigure(2, weight=1)

    def jump(self):
        """
        跳转页面
        :return:
        """
        self.root.destroy()
        MenuPage(root)


# 配置文件路径
file_path = r'D:/AddQQGroup/settings.xlsx'
qq_path = ''
is_execute = ''

# 初始化后台进程
p = multiprocessing.Process()

"""
登陆窗体
"""

root = Tk()

# 添加窗体关闭事件
root.protocol("WM_DELETE_WINDOW", close_window)

# 加载登陆窗体
LogPage(root)

# 显示界面
root.mainloop()







