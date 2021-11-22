from django.shortcuts import render
from django.contrib.auth.decorators import login_required

ERROR_PAGE = "/user/need_login"


@login_required(login_url=ERROR_PAGE)
def main(request):
    return render(request, "chatting.html")
