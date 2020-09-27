def score(word : str) -> int :
    #ここの形についての説明
    #https://qiita.com/icoxfog417/items/c17eb042f4735b7924a3

    point = 0
    string_new = []

    string_new = list(word.upper())
    point = points(string_new)
    return sum(point)


def points(string):
    point = []
    scores = [[1,{"A","E", "I", "O", "U", "L", "N", "R", "S", "T"}],
             [2,{"D", "G"}],
             [3,{"B", "C", "M", "P"}],
             [4,{"F", "H", "V", "W", "Y"}],
             [5,{"K"}],
             [8,{"J", "X"}],
             [10,{"Q", "Z"}]]
    for i in string:
        point += [j[0] for j in scores if i in j[1]]

    return point
