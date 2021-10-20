import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from community import service


def main(request):
    return render(request, "freeboard.html")


def write_page(request):
    return render(request, "write_article.html")


def write(request):
    if request.method == "POST":
        article_dict = json.loads(request.body)
        write_user_id = request.user.username
        write_contents = article_dict.get('contents')
        if article_dict.get('type') == "article":
            write_title = article_dict.get('title')
            service.create_article(write_user_id, write_title, write_contents)
        elif article_dict.get('type') == "comment":
            article_id = article_dict.get('article_id')
            service.create_comment(write_user_id, write_contents,article_id)

    return HttpResponse(status=200)


def edit_page(request):
    return render(request, "edit_article.html")


def edit(request, content_id):
    if request.method == "POST":
        comment_dict = json.loads(request.body)
        edit_contents = comment_dict.get('contents')
        if request.POST.get('type') == "article":
            edit_title = comment_dict.get('title')
            service.edit_article(content_id, edit_title, edit_contents)
        if request.POST.get('type') == "comment":
            service.edit_comment(content_id, edit_contents)

    return HttpResponse()


def delete(request, content_id):
    if request.POST.get('type') == "article":
        service.delete_article(content_id)
    if request.POST.get('type') == "comment":
        service.delete_comment(content_id)
    return HttpResponse()


def get_article_page(request, page_num):
    articles = service.get_article_list(page_num)
    article_list = [article for article in articles.values()]
    print(article_list)
    return JsonResponse({
        "articles": article_list
    })


def get_article(request, article_id):
    article = service.get_article(article_id)
    print(article.contents)
    return JsonResponse(json_dumps_params={"ensure_ascii": False}, data={
        'title': article.title,
        'contents': article.contents,
        'writer': article.user_id,
        'created_at': article.created_at})
