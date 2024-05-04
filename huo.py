xx=int(input())
kk=int(input())

# print(strx)
# print(stry)
def oror(a1, b1):
    a=a1[::-1]
    b=b1[::-1]
    c = []
    lenth = min(len(a), len(b))
    for i in range(0,lenth):
        if (int(a[i]) == 0 and int(b[i]) == 0):
            c.append('0')
        else:
            c.append('1')

    if len(a) < len(b):
        c += b[lenth:len(b)]
    else:
        c += a[lenth:len(a)]
    print(c[::-1])
    return c[::-1]

def judge(x,k):
    y = 1
    strx = bin(x).split('b')[1]
    stry = bin(y).split('b')[1]
    ki = 0
    while(y>0):
        xx = ''.join(bin(x + y).split('b')[1])
        yy = ''.join(oror(strx, stry))
        print(xx)
        print(yy)
        if xx== yy:
            ki=ki+1
            print(ki)
            if ki == k:
                print(y)
                return y
            else:
                y = y+1
        else:
            y=y+1
judge(xx,kk)






