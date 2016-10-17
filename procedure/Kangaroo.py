class Kangaroo:
    def __init__(self, name, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.pounch_contents = contents

    def put_in_pounch(self, obj):
        self.pounch_contents.append(obj)

    def __str__(self):
        t = [self.name+'pouch contents:']
        for obj in self.pounch_contents:
            s = " "+obj.__str__()
            t.append(s)
        return '\n'.join(t)

if __name__ == "__main__":
    kanga = Kangaroo("kanga")
    roo = Kangaroo("roo")
    roo.put_in_pounch("banana")
    kanga.put_in_pounch("apple")
    kanga.put_in_pounch("test")
    # kanga.put_in_pounch(roo)
    print(kanga)
    print(roo)