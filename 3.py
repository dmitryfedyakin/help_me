a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(sum(list(map(lambda n: n % c != 0 and n % 10 == d, range(a, b + 1)))))
