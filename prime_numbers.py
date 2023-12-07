number = range(1, 3000)


def is_prime(num):
    for numb in range(2, num):
        if num % 2 == 0:
            return False
    return True


primes = list(filter(is_prime, number))

print(primes)
