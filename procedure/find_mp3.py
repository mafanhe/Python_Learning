import os


def find_mp3(dirname):
    l = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            extension = filename.split('.')[-1]
            print(filename, extension)
            if extension == 'txt':
                l.append(os.path.join(root, filename))
    return l
            

if __name__ == "__main__":
    print(find_mp3("book/"))