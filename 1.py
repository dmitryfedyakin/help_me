def upper_case(letter):
  return letter == letter.upper()


i = int(input()) - 1
j = int(input())
sentence = input()
print(len(list(filter(upper_case, sentence[i:j]))))
