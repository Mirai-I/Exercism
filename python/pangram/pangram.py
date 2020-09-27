import string

def is_pangram(sentence:str)->bool:
    alphabet_list = list(string.ascii_lowercase)
    result = [True for alphabet in alphabet_list if alphabet in sentence.lower()]
    if len(result) ==26:
        return True
    else:
        return False
