from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

from community import service


def main(request):
    return render(request, "freeboard.html")


def write_page(request):
    return render(request, "write_article.html")


def write(request):
    if request.POST.get('type') == "article":
        write_user_id = request.user
        write_title = request.POST.get('title')
        write_contents = request.POST.get('contents')
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
    return JsonResponse({
        'title': article.title,
        'contents': article.contents,
        'writer': article.user_id,
        'created_at': article.created_at})
