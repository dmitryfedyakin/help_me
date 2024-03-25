import json

s = input()
data = json.loads(s)
print(sorted(data, key=lambda x: x[-1], reverse=True))
