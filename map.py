import sys
n = int(input())
ao = []

#mydict = {}
for j in range(0,n):
    ao.append(input())
# print(n)
# print(ao)

a = ao.copy()
resul = 0
for ite in range(0,len(a)):
    print("-----start-----")
    mydict = {}
    res = []
    resu = 0
    for ai in a:
        res1 = 0
        num = 9
        for i in ai:
            if i in mydict:
                break
            else:
                mydict[i] = num
            num = num -1
        sq = len(ai)
        for i in ai:
            res_tmp = pow(10, sq-1) * mydict[i]
            sq = sq-1
            res1= res1 + res_tmp
        res.append(res1)
    print(res)
    print(mydict)
    for kk in  res:
        resu = resu+kk
    print("resu: "+str(resu))
    if resul<resu:
        resul = resu
    a.pop(0)
    a.append(ao[ite])
    print(a)
print("resul: "+str(resul))