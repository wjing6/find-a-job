# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import copy

#lin 未入
#ll 栈内
#lout 已出
def f(lin:list, ll:list, lout:list):
    if len(lin) ==0:
        while len(ll) !=0:
            a=ll.pop()
            lout.append(a)
        result = ""
        for v in lout:
            result = result + " " +str(v)
        results.append(result[1:])
    else:
        if len(ll) ==0:
            f(lin[1:], ll+[lin[0]],lout)
        else:
            f(copy.copy(lin[1:]),copy.copy(ll + [lin[0]]), copy.copy(lout))
            f(copy.copy(lin), copy.copy(ll[:-1]), copy.copy(lout+[ll[-1]]))
            return


lin = list(input().split(' '))
#lout = list(input().split(' '))
results =[]
lout= []
ll = []
f(lin, ll, lout)
print(results)


if lout in results:
    print("1")
else:
    print("0")
