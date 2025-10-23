f=open ("texty.txt", "r", encoding="utf-8")
for line in f:
    print(line,end="")
    f.close ()
