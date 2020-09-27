def recite(start_verse, end_verse) -> int:
    gift =[]
    for i in range(start_verse -1 , end_verse):
        count = ["On the %s day of Christmas my true love gave to me: "  % chiffre(i)]
        count.extend(phrase(i))
        gift += [count]
    result =[]
    for j in gift:
        result +=[''.join(j)]
    return result

def chiffre(what_day):
    numbre_alphabet = ["first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"]
    return numbre_alphabet[what_day]

def phrase(what_day):
        phrase_day =["a Partridge in a Pear Tree.",
            "two Turtle Doves, ",
            "three French Hens, ",
            "four Calling Birds, ",
            "five Gold Rings, ",
            "six Geese-a-Laying, ",
            "seven Swans-a-Swimming, ",
            "eight Maids-a-Milking, ",
            "nine Ladies Dancing, ",
            "ten Lords-a-Leaping, ",
            "eleven Pipers Piping, ",
            "twelve Drummers Drumming, "]
        if what_day > 0:
            phrase_day[0] = "and a Partridge in a Pear Tree."

        new_list = list(reversed(phrase_day[:what_day+1]))
        return new_list
