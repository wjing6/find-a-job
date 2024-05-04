#  

def dp(money, wwei, v):
    nn = len(money)
    dp =[[0 for _ in range(v+1)]for _ in range(nn+1)]
    for nn in range(1,nn+1):
        for v in range(1,v+1):
            if v>= money[nn-1]:
                dp[nn][v] = max(dp[nn-1][v], dp[nn-1][v-money[nn-1]]+wwei[nn-1])
            else:
                dp[nn][v] = dp[nn-1][v]
    return dp[-1][-1]

# def dp(c:list, w:list,v:int):
#     a=len(c)
#     dp=[[0 for _ in range(v+1)]for _ in range(n+1)]
#     for index in range(n-1, -1,-1):
#         for rest in range(v+1):
#             p1 = dp[index+1][rest]
#             if rest-w[index]<0:
#                 nextindex = -1
#             else:
#                 nextindex = dp[index+1][rest-w[index]]
#             p2 =0
#             if nextindex != -1:
#                 p2 =c[index]+nextindex
#             dp[index][rest]=max(p1,p2)
#     return dp[n][v]

# for i in range(n):
#     m1, w1 = map(int, input().split(' '))
#     money.append(m1)
#     wei.append(w1)
#     wwei.append(w1*m1)
# print(dp(money, wwei, m))

money = [800, 400, 300,400,200]
wei = [2,5,5,3,2]
m = 1000
n = 5
for ii in range(len(money)):
    wwei.append(money[ii]* wei[ii])
#print(money)
print(dp(money, wwei, m))