'''
	https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
for a in range(1,1000):
    for b in range(a, 1000-a):
        c = 1000 - b - a:
        if a * a + b * b == c * c:
            print(a,b,c)
            print(f'Product is: {a*b*c}') #31875000