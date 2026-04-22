PHRASE = "Четные числа - питательные, а нечетные - просто вкусные"

P = 10009
Q = 10007
N = P * Q
PhiN = (P-1)*(Q-1)

E = 65537
D = pow(E, -1, PhiN)

encrypted = []
a = 0

#шифрование каждого символа
for char in PHRASE:
    m = ord(char)
    if m >= N:
        raise ValueError("Char is greater than N")
    c = pow(m, E, N)
    encrypted.append(c)

print(f"Зашифрованная фраза: {encrypted}")

#дешифрование каждого символа
decrypted_chars = []
for char in encrypted:
    m = pow(char, D, N)
    decrypted_chars.append(chr(m))

decrypted_phrase = "".join(decrypted_chars)

print(f"Расшифрованная фраза: {decrypted_phrase}")