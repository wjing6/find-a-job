
# x=int(input()).split(" ")
# y=int(input()).split(" ")

x = [1,2,3,5,3]
y = [1,2,3,4,5]

i =0
j= i+1
k=j+1
while i <len(x):
    j = i + 1
    while j<len(y):
        k = j + 1
        while k< len(x):
            if x[i]-x[j] ==0 and x[i]-x[k]==0:
                print(str(x[i]) + str(y[i]) +" and" +str(x[j]) + str(y[j])  +" and" +str(x[k]) + str(y[k]))
                continue
            elif x[i]-x[j]!= 0 and x[i]-x[k]!=0 and (y[i]-y[j])/(x[i]-x[j]) == (y[i]-y[k])/(x[i]-x[k]):
                print(str(x[i]) + str(y[i]) +" and" +str(x[j]) + str(y[j])  +" and" +str(x[k]) + str(y[k]))
            k=k+1
        j=j+1
    i=i+1

