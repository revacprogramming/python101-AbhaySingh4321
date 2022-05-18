# Lists

filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    
        for word in line:
            word=line.rstrip().split()
            if element in line:
                continue
            else :
                lst.append(element)
               

print(sort(lst))        

