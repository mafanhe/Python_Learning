# -*-coding:utf-8 -*-

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        """时间初始化
        :param hour: int
        :param minute: int
        :param second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print(str(self))

    def time_to_int(self):
        minutes = self.hour*60+self.minute
        seconds = minutes*60+self.second
        return seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = (self.time_to_int() + other.time_to_int())
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()+seconds
        return int_to_time(seconds)


def int_to_time(seconds):
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        return Time(hour, minute, second)
