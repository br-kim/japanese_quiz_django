import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from community import service


def main(request):
    return render(request, "freeboard.html")


def write_page(request):
    return render(request, "write_article.html")


def write(request):
    print(request.method)
    print(request.POST)
    if request.method == "POST":
        article_dict = json.loads(request.body)
        if article_dict.get('type') == "article":
            write_user_id = request.user.username
            write_title = article_dict.get('title')
            write_contents = article_dict.get('contents')
            service.create_article(write_user_id, write_title, write_contents)
    if request.POST.get('type') == "comment":
        pass

    return HttpResponse(status=200)


def edit_page(request):
    return render(request, "edit_article.html")


def edit(request, content_id):
    if request.POST.get('type') == "article":
        edit_title = request.POST.get('title')
        edit_contents = request.POST.get('contents')
        service.edit_article(content_id, edit_title, edit_contents)
    if request.POST.get('type') == "comment":
        pass

    return HttpResponse()


def delete(request, content_id):
    if request.POST.get('type') == "article":
        service.delete_article(content_id)
    if request.POST.get('type') == "comment":
        service.delete_comment(content_id)
    return HttpResponse()


def get_article_page(request, page_num):
    result = service.get_article_list(page_num)
    print([i for i in result.values()])
    return JsonResponse({
        "articles": [i for i in result.values()]
    })


def get_article(request, article_id):
    article = service.get_article(article_id)
    print(article.contents)
    return JsonResponse(json_dumps_params={"ensure_ascii":False}, data={
        'title': article.title,
        'contents': article.contents,
        'writer': article.user_id,
        'created_at': article.created_at})
