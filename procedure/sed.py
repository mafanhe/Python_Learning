
def sed(pattern, replace, source, dest):
    try:
        fin = open(source)
        fout = open(dest)
        for line in fin:
            line.replace(pattern, replace)
            fout.write(line)
    except:
        print("error")
    finally:
        fin.close()
        fout.close()