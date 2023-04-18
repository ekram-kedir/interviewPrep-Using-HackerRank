nums = list(input().split())
import math
a , b = int(nums[0]) , int(nums[1])

if b - a <= 1:
    print(math.gcd(a,b))
else:
    print(1)
