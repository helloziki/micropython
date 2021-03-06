# test integer floor division and modulo

# test all combination of +/-/0 cases
for i in range(-2, 3):
    for j in range(-4, 5):
        if j != 0:
            print(i, j, i // j, i % j, divmod(i, j))

# this tests compiler constant folding
print(123 // 7, 123 % 7)
print(-123 // 7, -123 % 7)
print(123 // -7, 123 % -7)
print(-123 // -7, -123 % -7)

# this tests bignum modulo
a = 987654321987987987987987987987
b = 19
print(a % b)
print(a % -b)
print(-a % b)
print(-a % -b)
