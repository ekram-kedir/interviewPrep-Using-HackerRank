import math

Test_cases = int(input())
for test in range(Test_cases):
    x =  int(input())
    y = 1
    if x == 1 or x == 2:
        print(3)
    elif x & 1 == 1 and x > 1:
        print(1)
    else:
        i = 1
        while x & i == 0:
            i = i << 1
        if i == x:
            print(i + 1)
        else:
            print(i)
