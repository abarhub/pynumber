from math import sqrt


def factorisation(n):
    # n=a*b
    # n=(a+b)*(a-b)
    # n=a^2-b^2
    # b^2=a^2-n
    # b^2=(x+c)^2-n avec x=n^.5

    x = int(sqrt(n))
    print(f'x={x}')
    for c in range(100):
        m = (x + c) ** 2 - n
        if m > 0:
            print('m=', m)
            g = int(sqrt(m))
            if g ** 2 == m:
                a = (x + c) + g
                b = (x + c) - g
                print(f'trouve: m={m}, x={x}, c={c}, n={n}, a={x + c}, b={g}, n={a}*{b}')
                return


factorisation(893)
# factorisation(15)
# factorisation(799)
