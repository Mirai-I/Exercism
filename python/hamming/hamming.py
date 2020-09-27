def distance(strand_a, strand_b):
    #returnは異なるアルファベットの数
    n = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Meaningful message indicating the source of the error")
    #try:
    for a,b in zip(strand_a,strand_b):
        if a != b:
            n +=1
    return n

    # except ValueError as error:
    #     raise ValueError("Meaningful message indicating the source of the error")
    #     pass

#zipは結構for文の中で使われる
#https://teratail.com/questions/149532

#ZIPの基本
#https://python.civic-apps.com/zip-enumerate/
