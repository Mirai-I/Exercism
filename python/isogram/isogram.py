import re
import string as str

def is_isogram(string):
    # 単語の中にアルファベットが1回のみ入っている単語のこと
    #　ハイフンとか空白はOK

    # ハイフンやそのほかの記号を全削除
    string = string.translate(string.maketrans("","",str.punctuation)).replace(" ", "")

    string_list = list(string.lower())
    if len(string_list) == 0:
        return True

    for i in string_list:
        if string.lower().count(i) > 1:
            return False

    return True
