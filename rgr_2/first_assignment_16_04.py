import math

#проверка на взаимную простоту для n
def check_is_all_prime(numbers):
    for i in range(0, len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            gcd = math.gcd(numbers[i], numbers[j])
            if gcd != 1:
                raise Exception('Prime numbers not all prime')

#проверка остатков r
def check_is_all_remainders(numbers, primes):
    if len(numbers) != len(primes):
        raise Exception('Remainders and primes count should be equal')

    for i in range(0, len(numbers)):
        if numbers[i] >= primes[i]:
            raise Exception('Remainder is more or equal prime')

#поиск взаимно обратного для n по модулю mod
def find_mutually_inverse(n, mod):
    for Mi in range(1, mod):
        if (n * Mi) % mod == 1:
            return Mi
    raise Exception('Not found a Mi')

print("Введите n:")
prime_numbers = list(map(int, input().split()))
check_is_all_prime(prime_numbers)

print("Введите r:")
remainders = list(map(int, input().split()))
check_is_all_remainders(remainders, prime_numbers)

N = 1
for el in prime_numbers:
    N *= el

X = 0
for i in range(len(prime_numbers)):
    Ni = N // prime_numbers[i]
    Ri = remainders[i]
    Mi = find_mutually_inverse(Ni, prime_numbers[i])

    X += Ni * Mi * Ri

print("Решения:", X, "и", X % N)
