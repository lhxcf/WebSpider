#     下载相关软件：    pc端对应：
#              夜神模拟器  ->  谷歌浏览器    (https://www.yeshen.com)
#               Node.js  ->  安装软件所用的插件    (https://nodejs.org/zh-cn/download/)   验证是否安装成功：cmd中输入 “node -v”
#                   JDK  ->  安装软件所用的插件    (https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)
#        Android Studio  ->  安装软件所用的插件    (https://www.androiddevtools.cn/)
#                Appium  ->  Selenium库中用到的模拟浏览器ChromeDriver    (http://appium.io/)
# Appium-Python-Client库  ->  Selenium库
# 安装JDK主要是为了方便之后安装Android Studio和Appium，两者都需要Java环境
# Android Studio安装：进入网站后，Android SDK工具 -> SDK Tools
# 安装后启动安装文件夹内的SDK Manager.exe,勾选安装Tools的前三个、Extras中的Android Support Repository 和 Google USB Driver
# 在cmd命令窗口运行指令：connect 127.0.0.1:62001,使用adb devices 检验是否连接成功
# 用adb查看App信息：（1）adb shell    （2）dumpsys activity | grep mFocusedActivity
#
