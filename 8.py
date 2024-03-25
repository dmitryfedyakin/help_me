from datetime import datetime


def logf_in(func):

  def wrapped(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except Exception as error:
      with open('log_file.log', 'a') as f:
        f.write(f'{datetime.now()} выдано исключение {type(error).__name__}\n')

  return wrapped


@logf_in
def division(a, b):
  return a / b


@logf_in
def type_error(a, b):
  return a + b


division(10, 0)
type_error(10, 'errors')
