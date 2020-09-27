import string as str
import re
import itertools

def count_words(sentence):
    sentence_remove =[]
    data =[]
    same = []

    words = sentence.split()
    words = [i.strip("''") for i in words]

    for i in words:
        sentence_remove +=re.findall(r'([^.:_,!@$%^&]+)', i.lower())

    for word in sentence_remove:
        data += [[word,sentence_remove.count(word)]]

    for position in sentence_remove:
        l =[i for (i, x) in enumerate(sentence_remove) if x == position]
        if len(l)>1:
            if not l in same:
                same += [l]

    for position_remove in same:
        del position_remove[0]

    new_same = sorted(list(itertools.chain.from_iterable(same)),reverse=True)

    for de in new_same:
        del data[de]

    return {word[0]: word[1] for word in data}
