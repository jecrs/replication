for c in next(os.walk("commands"))[2]:
    lib = __import__("commands."+c[:-3])
    if hasattr(getattr(lib,c[:-3]),"Handler"):
        pass
    else:
        print("o {} não e um comando :(".format(c))