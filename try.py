def combination(n, k):
    """
    自定义函数
    """
    global count     # 定义全局变量,即主函数中的count和此自定义函数中的count一样，是1就都是1
    if k < 0 or n <= 0 or k > n:
        print("error")
    elif k == 0:
        print('1', end='')  # end=''表示此行末不换行
    else:
        x = 1
        y = 1
        for i in range(n-k+1, n+1):  # 此处的i和主函数中的i不是同一个i，相互独立
            x = x * i
        for j in range(1, k + 1):
            y = y * j
        print(f' + {x / y}x^{count}', end='')  # 修改后的代码，用于格式化输出，满足问题三的要求
    count += 1


# 主函数

count = 0   # 添加的代码,用于计数
num = 4
for i in range(0, num+1):
    combination(num, i)
