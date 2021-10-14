import os
import random

hiragana_dir = "./static/img/hiragana"
katakana_dir = "./static/img/katakana"
hiragana_dir_list = [f".{hiragana_dir}/{file_name}" for file_name in os.listdir(hiragana_dir)]
katakana_dir_list = [f".{katakana_dir}/{file_name}" for file_name in os.listdir(katakana_dir)]


def get_gana_url(gana=None):
    if gana == "hiragana":
        return random.choice(hiragana_dir_list)
    elif gana == "katakana":
        return random.choice(katakana_dir_list)
    else:
        return random.choice(hiragana_dir_list + katakana_dir_list)


def get_gana_url_list(gana=None):
    if gana == "hiragana":
        return random.sample(hiragana_dir_list, len(hiragana_dir_list))
    elif gana == "katakana":
        return random.sample(katakana_dir_list, len(hiragana_dir_list))
    else:
        return random.sample(hiragana_dir_list + katakana_dir_list, len(hiragana_dir_list+katakana_dir_list))
