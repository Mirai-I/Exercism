import re
class Matrix:
    def __init__(self, matrix_string):
        #self = matrix_string
        matrix_int = [i.split() for i in matrix_string.split('\n')]
        self.matrix_string = []
        for i in matrix_int :
            self.matrix_string += [[int(j) for j in i]]

    def row(self, index):
        #selfは元のマトリックスinitで定義済み，indexは元のマトリックスの横の何列目を出してほしいか
        return self.matrix_string[index-1]

    def column(self, index):
        #縦向き
        return [row[index - 1] for row in self.matrix_string]

        # これはお世話になった
        # https://ct-innovation01.xyz/DL-Freetime/python01/
