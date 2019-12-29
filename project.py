import sys
sent = input()
listsent = str.split(sent, ' ')
alist = []
for i in range(len(listsent)):
    blist = []
    w=len(listsent[i])
    print (w)
    for j in range(w):
        blist.append(listsent[i][w-1-j])
    alist.append(blist)
clist = []
for i in range(len(alist)):
    clist.append(''.join(alist[i]))
done = ' '.join(clist)
print (done)