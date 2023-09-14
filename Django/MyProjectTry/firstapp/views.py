from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):

    # 使用HttpResponse只能返回文本
    # return HttpResponse("你好呀")

    # render函数，根据app注册顺序，在templates目录下查找网页
    return render(request, 'index.html')



