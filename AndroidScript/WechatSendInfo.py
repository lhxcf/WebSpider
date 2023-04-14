import uiautomator2 as u2

# 连接安卓设备
d = u2.connect()

# 启动微信 app
d.app_start("com.tencent.mm")

# 等待微信 app 启动
d(resourceId="com.tencent.mm:id/azk").wait(timeout=20)

# 点击“通讯录”按钮
d(resourceId="com.tencent.mm:id/hk").click()

# 等待通讯录页面加载
d(resourceId="com.tencent.mm:id/b5k").wait(timeout=20)

# 找到备注为“张三”的好友
friend = d(text="妈")

# 点击该好友
friend.click()

# 等待聊天页面加载
d(resourceId="com.tencent.mm:id/a_0").wait(timeout=20)

# 在输入框中输入要发送的信息
d(resourceId="com.tencent.mm:id/aqe").set_text("你好，这是一条测试信息")

# 点击发送按钮
d(resourceId="com.tencent.mm:id/aqf").click()

# 关闭微信 app
d.app_stop("com.tencent.mm")
