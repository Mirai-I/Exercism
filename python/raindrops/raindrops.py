def convert(number):
    #multiple = [3,5,7]
    factor = [[3,"Pling"],[5,"Plang"],[7,"Plong"]]
    result = str()

    try:
        for i in factor:
            if number % i[0] == 0:
                result += i[1]

        if not result:
            result += str(number)

        return result

    except Exception as e:
        raise Exception("Meaningful message indicating the source of the error")
        pass

# 2次元配列
# https://www.sejuku.net/blog/67215
#
# for文2次元配列
# https://www.sejuku.net/blog/24766
#
# 配列空白判定
# https://www.mathpython.com/ja/python-list-empty/
#
# 演算子
# https://hibiki-press.tech/learn_prog/python/divmod/3541#%25_%E6%BC%94%E7%AE%97%E5%AD%90%EF%BC%88x_%25_y%EF%BC%89
