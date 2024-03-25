import json
import xml.etree.ElementTree as ET
import yaml


def to_format(file_type='json'):

  def decorator(func):

    def wrapped(*args, **kwargs):
      result = func(*args, **kwargs)
      if file_type == 'xml':
        if isinstance(result, str):
          root = ET.Element('root')
          ET.SubElement(root, 'data').text = str(result)
          return ET.tostring(root)
        if isinstance(result, dict):
          root = ET.Element('root')
          for key, value in result.items():
            ET.SubElement(root, key).text = str(value)
          return ET.tostring(root)
        if isinstance(result, list):
          root = ET.Element('root')
          for item in result:
            ET.SubElement(root, 'data').text = str(item)
          return ET.tostring(root)
      elif file_type == 'yaml':
        return yaml.dump(result)
      else:
        return json.dumps(result)

    return wrapped

  return decorator


@to_format()
def simple_str():
  return 'My name is Dima'


@to_format('xml')
def order_dict(name, phone):
  return {'Name': name, 'Phone number': phone}


@to_format('yaml')
def number_list():
  return [1, 3, 5, 7, 6, 4, 2]


print(simple_str())
print(order_dict('Alex', '2-17-75'))
print(number_list())
