
def response(hey_bob:str) -> str:

    if ("?" in hey_bob and hey_bob.isupper()) :
            return "Calm down, I know what I'm doing!"
    elif (hey_bob.isupper() or ("!" in hey_bob and hey_bob.isupper())) :
        return "Whoa, chill out!"
    elif hey_bob.split() ==[]:
        return "Fine. Be that way!"
    elif "?" == hey_bob.split()[-1][-1] :
        return "Sure."
    else:
        return "Whatever."
