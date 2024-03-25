import functools

a = int(input())
b = int(input())
c = int(input())

list_1 = [n for n in range(a, b + 1) if int(n**0.5)**2 == n and n % c == 0]
print(functools.reduce(lambda x, y: x * y, list_1))
