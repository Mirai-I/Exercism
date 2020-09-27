# https://note.nkmk.me/python-re-match-search-findall-etc/
# https://docs.python.org/ja/3/library/re.html#regular-expression-syntax
# reの使い方の説明
import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self) -> bool:
        if re.search(r'([-.:_,!@$%^&]+)',self.card_num) or re.search(r'[A-Za-z]+',self.card_num):
            return False
        numbre = re.findall(r'\d', self.card_num)
# int にしていない
        len_numbre = len(numbre)
        numbre = [int(numbre[i]) for i in range(len_numbre)]
        if len_numbre == 1:
            return False
        
        for i in range(len_numbre-2, -1, -2):
            if numbre[i] * 2 > 9:
                numbre[i] = numbre[i] * 2 - 9
            else:
                numbre[i] = numbre[i] * 2

        if sum(numbre) % 10 == 0:
            return True
        else:
            return False
