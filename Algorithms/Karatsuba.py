def karatsuba(x, y, b=10):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        p = max(len(str(x)), len(str(y))) // 2

        a = x // b**(p)
        w = x % b**(p)
        c = y // b**(p)
        d = y % b**(p)

        t1 = karatsuba(a, c)
        t2 = karatsuba((a + w), (c + d))
        t3 = karatsuba(w, d)

        return (t1 * b**(2 * p)) + ((t2 - t1 - t3) * b**(p)) + (t3)


print(karatsuba(1234, 2121))
print(karatsuba(4567, 3498))
