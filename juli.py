# a=input()
# b=input()


def dist(a, b):
    if len(a)==0 or len(b) ==0:
        return max(len(a), len(b))
    elif a[len(a)-1]==b[len(b)-1]:
         return dist(a[:len(a)-1],b[:len(b)-1])
    else:
        return min(dist(a[:len(a)-1],b), dist(a,b[:len(b)-1]),dist(a[:len(a)-1],b[:len(b)-1])) +1

print(dist("abcdefcccccg", "abcdef"))



def dist2(a, b):
    m = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
    for i in range(len(b)+1):
        m[i][0] = i
    for j in range(len(a)+1):
        m[0][j] = j

    for i in range(1,len(b)+1):
        for j in range(1,len(a)+1):
            if b[i-1] ==a[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) +1
    return m

print(dist2("ab", "abcdddd"))
