import json


def to_json(func):

  def wrapped(*args, **kwargs):
    result = func(*args, **kwargs)
    return json.dumps(result)

  return wrapped


@to_json
def person_dict(name, height, weight):
  return {'Your name': name, 'Your height': height, 'Your weight': weight}


@to_json
def letter_list():
  return ['A', 'E', 'I', 'O', 'U', 'Y']


print(person_dict('Alex', 191, 80))
print(letter_list())
