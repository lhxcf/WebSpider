import datetime

import psutil
import subprocess
import pyautogui as pt
import time
import webbrowser
import threading


class AddGroup:
    def __init__(self, urls):
        """
        初始化AddGroup类
        :param urls: 存放所有url的列表
        """
        self.urls = urls
        self.lock = threading.Lock()
        self.is_open_url = False

    def __click_next(self, current_win, close_win=False):
        """
        点击"下一步"按钮，实现自动加群
        :param current_win: 当前”添加群“窗体
        :return:
        """
        current_win.size = (705, 554)
        current_win.click(current_win.left + 500, current_win.bottom - 30)

        print("点击一次")
        if close_win:
            current_win.close()

    def add_all_group(self, title, close_win=False):
        """
        多线程点击所有窗体，实现加入所有群
        :param title: 要筛选的窗体标题
        :param close_win: 是否在点击完成后关闭窗体
        :return:
        """
        current_wins = pt.getWindowsWithTitle(title)
        # 创建线程列表，点击每个窗体的”下一步“
        threads = []
        for current_win in current_wins:
            thread = threading.Thread(target=self.__click_next, args=(current_win, close_win,))
            thread.start()
            threads.append(thread)

        count = 0
        # 等待所有线程执行完成
        for thread in threads:
            count += 1
            thread.join()
            print(f'加入第{count}进程, {datetime.time}')

    def __open_url(self, url):
        """
        使用webbrowser利用默认浏览器打开url
        :return:
        """
        try:
            with self.lock:
                webbrowser.open(url)
                self.is_open_url = True
        except :
            pass

    def open_all_url(self):
        """
        利用多线程打开urls中所有的url
        :return: bool->是否成功打开url
        """

        try:
            # 创建线程列表
            threads = []

            # 遍历url列表，创建并启动线程
            for url in self.urls:
                thread = threading.Thread(target=self.__open_url, args=(url,))
                thread.start()
                threads.append(thread)

            # 等待所有线程执行完毕
            for thread in threads:
                thread.join()
            return self.is_open_url
        except :
            return self.is_open_url

    # 检查QQ是否启动
    def __is_qq_running(self):
        """
        检查QQ是否启动
        :return:
        """
        for proc in psutil.process_iter(['name']):
            if proc.name() == 'QQ.exe':
                return True
        return False

    # 启动QQ
    def __start_qq(self, qq_path):
        """
        启动QQ
        :param qq_path: QQ快捷方式的绝对路径
        :return:
        """
        subprocess.Popen(qq_path)
        time.sleep(10)

    def check_qq_status(self, qq_path):
        """
        检查qq登陆状态，若未登录则启动qq并登陆
        :param qq_path: QQ快捷方式的绝对路径
        :return:
        """
        if not self.__is_qq_running():
            try:
                self.__start_qq(qq_path)
            except:
                self.show_message("启动QQ失败，请先设置QQ为自动登陆！")

    @staticmethod
    def show_message(message):
        """
        消息框（仅消息）
        :param message: 消息内容
        :return:
        """
        pt.alert(message)

    @staticmethod
    def show_confirm(message):
        """
        OK/Cancel消息框
        :param message: 消息内容
        :return: OK/Cancel
        """
        return pt.confirm(message)

    @staticmethod
    def show_prompt(message):
        """
        对话框
        :param message: 信息内容
        :return: 文本框填入的内容
        """
        return pt.prompt(message)

    @staticmethod
    def show_password(message):
        """
        对话框
        :param message: 信息内容(对话框显示***)
        :return: 文本框填入的内容
        """
        return pt.password(message)
