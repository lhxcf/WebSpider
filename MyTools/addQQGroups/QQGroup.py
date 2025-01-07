from AddQQGroup.AddGroupTools import AddGroup
from AddQQGroup.SettingTools import SettingTools
import datetime
import time


def add_qq_group(qq_path, file_path):
    """
    利用多线程方式实现某一时刻同时提交多个群聊申请,请先验证file_path文件存在
    :param qq_path: QQ快捷方式的绝对路径
    :param file_path: 文件名称
    :return:bool 进程是否添加成功
    """
    # 检查、读取配置文件
    data = check_setting_exit(file_path)

    # 初始化AddGroup对象，检查QQ登陆状态
    urls = data[0]
    qq = AddGroup(urls)
    qq.check_qq_status(qq_path)
    # 打开所有url，即所有”添加群“框
    is_open_url = qq.open_all_url()
    if not is_open_url:
        AddGroup.show_message("der~呆子！群聊链接没打开！你是不是配置文件还没给我喂QQ群连接呢！！！")

    # 获取日期，并处理日期格式
    try:
        date_sets = data[1][0].split('/')
        date_sets = list(map(int, date_sets))
        # 设置目标日期和时间
        target_date = datetime.datetime(date_sets[0], date_sets[1], date_sets[2], date_sets[3], date_sets[4],
                                        date_sets[5])

        if target_date < datetime.datetime.now():
            AddGroup.show_message("请检查配置文件是否正确填写加群日期！")
            return False

        # 循环检查当前日期和时间，直到达到目标日期和时间
        time_spen = (target_date - datetime.datetime.now()).seconds
        if time_spen > 10:
            time.sleep(time_spen - 10)
        while datetime.datetime.now() < target_date + datetime.timedelta(seconds=15):
            # 打开加群界面
            qq.open_all_url()

            # 点击加群
            qq.add_all_group("添加群", True)
    except:
        AddGroup.show_message("请检查配置文件是否正确填写加群日期！")
        return False
    return True


def check_setting_exit(file_path):
    """
    检查配置文件路径
    :param file_path: 配置文件路径
    :return:
    """
    # 检查配置文件
    data = SettingTools.check_setting_file(file_path)
    if data is None:
        AddGroup.show_message(f"已在{file_path}下创建配置文件，请在文件中填写要加入群聊的链接，也可修改相应配置信息！")
    return data


if __name__ == "__main__":
    # 系统内qq快捷方式路径
    qq_path_ = r'D:\software\QQ\Bin\QQScLauncher.exe'
    f_path = r'D:/AddQQGroup/settings.xlsx'
    add_qq_group(qq_path_, f_path)

