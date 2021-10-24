import json

from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from community import service


@login_required()
def main(request):
    return render(request, "freeboard.html")


@login_required()
def write_page(request):
    return render(request, "write_article.html")


@login_required()
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
            parent_id = article_dict.get('parent_id')
            service.create_comment(write_user_id, write_contents, article_id, parent_id)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=405)


@login_required()
def edit_page(request):
    return render(request, "edit_article.html")


@login_required()
def edit(request, content_id):
    if request.method == "PATCH":
        comment_dict = json.loads(request.body)
        edit_contents = comment_dict.get('contents')
        print(comment_dict)
        if comment_dict.get('type') == "article":
            edit_title = comment_dict.get('title')
            service.edit_article(content_id, edit_title, edit_contents)
        if comment_dict.get('type') == "comment":
            service.edit_comment(content_id, edit_contents)

        return HttpResponse(status=204)
    else:
        return HttpResponse(status=405)


@login_required()
def delete(request):
    body = json.loads(request.body)
    content_id = body.get('content_id')
    print(body.get('content_writer'), request.user.username)
    if body.get('content_writer') == request.user.username:
        if request.method == "DELETE":
            if body.get('type') == "article":
                service.delete_article(content_id)
            if body.get('type') == "comment":
                service.delete_comment(content_id)
            return HttpResponse(status=204)
        else:
            return HttpResponse(status=405)
    return HttpResponse(status=403)


@login_required()
def get_article_list(request, page_num):
    articles = service.get_article_list(page_num)
    article_list = [article for article in articles.values()]
    return JsonResponse({
        "articles_length": service.get_articles_size(),
        "articles": article_list,
    })


@login_required()
def get_article(request, article_id):
    article = service.get_article(article_id)
    return JsonResponse(json_dumps_params={"ensure_ascii": False}, data={
        'title': article.title,
        'contents': article.contents,
        'writer': article.user_id,
        'created_at': article.created_at})


@login_required()
def get_comments(request, article_id):
    comments = service.get_comments(article_id)
    return JsonResponse({"comments": [comment for comment in comments.values()]})


@login_required()
def article_page(request):
    return render(request, "article.html")
