a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = filter(lambda num: num % c == 0 and num % d == 0, range(a, b + 1))
print(sum(list(result)))
