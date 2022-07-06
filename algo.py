""" 
Given a positive sorted array:
a = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ];
Define a function f(a, x) that returns x, the next smallest number, or -1 for errors.

i.e.
f(a, 12) = 12
f(a, 13) = 12

Additional constraints:
len(array) < 100
array vals between -1000 and 1000
"""
def f(a, x):
    try:
        if (not a or x < a[0]):
            return -1

        left = 0 
        right = len(a)-1
        
        # short circuit: x >= max value, return next smallest
        if (x>=a[right]):
            return a[right]

        # short circuit: x = min value, return min
        if (x == a[left]):
            return a[left]

        while (right - left > 1):
            middle = left + (right - left)//2
            
            # case: we have x, just return it
            if a[middle] == x: 
                return x
            # case: x < middle, reset upper index
            elif x < a[middle]:
                right = middle - 1
            # case: x > middle, reset lower index
            else:
                left = middle

            # the target element x is not in the array 
            # so we return the next smallest value
            return a[left] 
    except:
        return -1