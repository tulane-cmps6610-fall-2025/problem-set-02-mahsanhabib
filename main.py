"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    ### TODO
    # Pad both x and y to the same even length
    xvec, yvec = pad(x.binary_vec, y.binary_vec)
    n = len(xvec)
    # Now split
    xl, xr = split_number(x.binary_vec)
    yl, yr = split_number(x.binary_vec)

    # Compute the three products
    first = bit_shift(BinaryNumber(xl.decimal_val * yl.decimal_val), n)
    second = bit_shift(BinaryNumber(xl.decimal_val * yr.decimal_val + xr.decimal_val * yl.decimal_val), n//2)
    third = bit_shift(BinaryNumber(xr.decimal_val * yr.decimal_val), 0)
    max_len = max(len(first.binary_vec), len(second.binary_vec), len(third.binary_vec))
    first.binary_vec = ['0'] * (max_len - len(first.binary_vec)) + first.binary_vec
    second.binary_vec = ['0'] * (max_len - len(second.binary_vec)) + second.binary_vec
    third.binary_vec = ['0'] * (max_len - len(third.binary_vec)) + third.binary_vec
    # print(first, second, third)
    # Add the three binary numbers (as vectors) together
    def add_binary_vecs(a, b):
        # a, b are lists of '0'/'1'
        max_len = max(len(a), len(b))
        a = ['0'] * (max_len - len(a)) + a
        b = ['0'] * (max_len - len(b)) + b
        carry = 0
        result = ['0'] * max_len
        for i in range(max_len-1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            result[i] = str(total % 2)
            carry = total // 2
        if carry:
            result = [str(carry)] + result
        return result

    sum1 = add_binary_vecs(first.binary_vec, second.binary_vec)
    total_sum = add_binary_vecs(sum1, third.binary_vec)
    return binary2int(total_sum)
    # print(x.binary_vec, xl, xr)
    ###

def subquadratic_multiply(x, y):
    ### TODO
    pass
    ###

## Feel free to add your own tests here.
def test_multiply():
    assert binary2int(quadratic_multiply(BinaryNumber(2), BinaryNumber(2))) == 2*2

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f 
    print(f(x,y))
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
    

compare_multiply()