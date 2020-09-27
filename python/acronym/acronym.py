import re
import itertools

def abbreviate(words):
    word_new =[]
    output = []

    word_new = [re.findall(r'([^.:_,!@$%^&-]+)', i.upper()) for i in words.split()]
    word_new = list(itertools.chain.from_iterable(word_new))

    for i in word_new:
        output.append(i[0][0])

    return ("").join(output)
