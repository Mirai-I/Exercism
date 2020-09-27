# 特殊メソッドに関して
# https://blog.codecamp.jp/python-class-code
# 文字のフォーマットに関して
# https://gammasoft.jp/blog/python-string-format/
class Clock:
    def __init__(self, hour = 0, minute =0):
        self.hour = (hour + minute//60) %24
        self.minute = minute % 60
#        self.clock = datetime.time(hour, minute)

    def __repr__(self):
        # outputを勝手にするみたいな？
#        return self.clock.strftime("%H:%M")
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        # other もselfと同じ使い方ができる（この特殊メソッドの場合）
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour,self.minute + minutes)

    def __sub__(self, minutes):
        return self.__add__(-1 * minutes)

#参考
#https://exercism.io/tracks/python/exercises/clock/solutions/3bdf3a25a4784bdcbec127ae60d8a390
