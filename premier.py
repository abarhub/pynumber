def isprime(number: int) -> bool:
    for i in range(2, number):
        if i >= number:
            break
        elif number % i == 0:
            return False
    return True


print('liste de nombres premiers')
for x in range(2, 100000):
    if isprime(x):
        print(x)
