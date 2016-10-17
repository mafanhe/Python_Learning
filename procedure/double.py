import datetime


def now():
    now = datetime.datetime.today()
    print(now.weekday())

def birthday(birthday):
    now = datetime.datetime.today()
    age = now - birthday
    next_birthday = datetime.datetime(now.year, birthday.month, birthday.day)
    if now > next_birthday:
        next_birthday = datetime.datetime(now.year+1, birthday.month, birthday.day)
    print((next_birthday-now).days)


def double(birthday1,birthday2):
    pass


if __name__ == "__main__":
    birthday(datetime.datetime(1992,10,24))
