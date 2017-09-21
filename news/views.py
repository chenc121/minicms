# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from news.models import Column
from news.models import Article
from django.shortcuts import redirect
from django.http import JsonResponse
from django.template import RequestContext


def index(request):
    columns = Column.objects.all()
    # return redirect("http://www.ziqiangxuetang.com/django/django-cms-develop3.html")
    # return render(request, 'index.html', {'columns': columns})
    return render(request, 'index.html')


def column_detail(request, column_slug):
    # return HttpResponse('colmun slug: ' + column_slug)
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect("http://www.ziqiangxuetang.com/django/django-cms-develop3.html")
    return render(request, 'news/article.html', {'article': article})


def template_index_reports(request):
    reports_tmp_return = 'kkkkk'
    return JsonResponse(reports_tmp_return, safe=False)


def file_upload(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("uploadBox", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render(request, 'index.html', {'uploadResult':"no files for upload!"})
        import os
        destination = open(os.path.join("D:\\TDDOWNLOAD", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
            destination.close()
            # return render(request, 'index.html', {'uploadResult':"glyphicon glyphicon-ok-circle"})
        return render(request, '', {'uploadResult': "file"})


def file_upload_json(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("uploadBox", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            result = 'none'
            return JsonResponse(result, safe=False)
        import os
        destination = open(os.path.join("D:\\TDDOWNLOAD", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        result = 'success'
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
            destination.close()
            # return render(request, 'index.html', {'uploadResult':"glyphicon glyphicon-ok-circle"})
        #return JsonResponse(result, safe=False)
        import json
        return HttpResponse(json.dumps(result))


def file_upload_fileinput(request):
    result = {"data": []}
    try:
        ret = -1
        myfile = request.FILES.get("file_data", None)
        if myfile:
            import os
            destination = open(os.path.join("D:\\TDDOWNLOAD", myfile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            if not myfile:
                ret = 1
            ret = 0
        return JsonResponse(result)
    except Exception:
        return JsonResponse(result)