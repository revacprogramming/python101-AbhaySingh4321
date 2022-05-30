# Dictionaries
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di=dict()
for lin in handle:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
            
largest=-1
theword=None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k
print(theword,largest)        
