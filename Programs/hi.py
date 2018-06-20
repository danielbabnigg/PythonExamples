okcount = 0
with open("hi.txt", "w+") as ok:
    while okcount < 1000:
        ok.write("ok" + "\n")
        okcount += 1