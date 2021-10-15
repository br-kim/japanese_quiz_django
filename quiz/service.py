from quiz import models


def create_score(_user_id):
    return models.Score.objects.create(user_id=_user_id)


def update_score(kind, character, _user_id):
    if kind == "hiragana":
        score = models.Score.objects.get(user_id=_user_id)
        if score.hiragana_score.get(character):
            score.hiragana_score[character] += 1
        else:
            score.hiragana_score[character] = 1
        score.save()

    elif kind == "katakana":
        score = models.Score.objects.get(user_id=_user_id)
        if score.katakana_score.get(character):
            score.katakana_score[character] += 1
        else:
            score.katakana_score[character] = 1
        score.save()

    else:
        raise ValueError
