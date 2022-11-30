def read_ints(fname):
    for line in open(fname):
        yield int(line)
        
def read_line(fname):
    for line in open(fname):
        yield (line.split())

h=0
d=0

for (command, distance) in read_line('input-1'):
    if command == 'forward':
        h = h+int(distance)
    elif command == 'down':
        d = d+int(distance)
    elif command == 'up':
        d = d-int(distance)
    else:
        print("incorrect comand")
print("Horizontal ",h)
print("Distance ",d)
print("Answer ",h*d)

#i = 0
#for (count, n) in enumerate(read_ints('input-1')):
#    if count == 0:
#        print(n, " N/A - No previous")
#    else:
#        if n > p :
#            print(n, " increasing")
#            i +=1
#        elif n<p:
#            print(n, " decreasing")
#        else:
#            print(n, "same")
#    p = n
#print(i, "Increasing")