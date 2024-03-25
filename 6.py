def result_out(func):

  def wrapped(number):
    result = func(number)
    print(result)
    return result

  return wrapped


@result_out
def root(num):
  return num**0.5


@result_out
def even_odd(num):
  return 'Четное' if num % 2 == 0 else 'Нечетное'


@result_out
def square(num):
  return num**2


n = int(input())
root(n)
even_odd(n)
square(n)
