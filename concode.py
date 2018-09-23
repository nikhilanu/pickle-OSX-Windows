
#Module for editing passcode

import random
lst = [3142, 1999, 1618, 6174, 2718, 5772, 4669, 1010, 8675, 5309, 9991, 3636, 3371, 7912, 1246]



def  userpass(n):
    num=str(n)
    x=num[len(num)-1]
    encry_pass=n+lst[int(x)]
    return encry_pass

