def read_ints(fname):
    for line in open(fname):
        yield int(line)

i = 0
for (count, n) in enumerate(read_ints('input-1')):
    if count == 0:
        print(n, " N/A - No previous")
    else:
        if n > p :
            print(n, " increasing")
            i +=1
        elif n<p:
            print(n, " decreasing")
        else:
            print(n, "same")
    p = n
print(i, "Increasing")
