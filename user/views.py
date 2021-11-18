from django.shortcuts import render
from django.http.response import HttpResponseRedirect

from .form import UserRegistrationForm
from .service import register_user
from quiz.service import create_score, get_score


def create_user_page(request):
    if request.method == "GET":
        user_registration_form = UserRegistrationForm()
    else:
        user_registration_form = UserRegistrationForm(request.POST)
        if user_registration_form.is_valid():
            register_user(user_id=user_registration_form.cleaned_data['user_id'],
                          user_email=user_registration_form.cleaned_data['user_email'],
                          user_password=user_registration_form.cleaned_data['user_password'])
            create_score(user_registration_form.cleaned_data['user_id'])
            return HttpResponseRedirect('/')

    context = {
        'form': user_registration_form
    }
    return render(request, "create_user_page.html", context)


def delete_user():
    return


def edit_user():
    return


def user_profile(request):
    return render(request, "user_profile.html")


def user_scoreboard(request):
    score = get_score(request.user)
    return render(request, "scoreboard.html",
                  context={"hiragana_score": score.get('hiragana_score'),
                           "katakana_score": score.get('katakana_score')})


def need_login(request):
    return render(request, "error.html", context={"message": "로그인이 필요합니다."})
