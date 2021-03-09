# AUTOGENERATED! DO NOT EDIT! File to edit: dictUtil.ipynb (unless otherwise specified).

__all__ = ['printDict', 'allKeysInDict', 'filterDt', 'stripDict', 'hashDict', 'saveDictToFile', 'loadDictFromFile',
           'saveStringToFile', 'loadStringFromFile', 'genSchema']

# Cell
# from datetime import datetime

# Cell
def printDict(d:dict, length:int = 10, space = 0):
  '''print dictionary as first x value of values'''
  if type(d) != dict:
    print('this is not a dict')
    print(d)
  else:
    for k, v in d.items():
      if type(v) == dict:
        print(f"{' '*space}{k}")
        printDict(v, space=space+1)
      else:
        print(f"{' '*space}{k} : {v[:length] if type(v)==str else v}")

# Cell
def allKeysInDict(inputDict:dict, keys:list):
  return all(key in inputDict for key in keys)

# Cell
def filterDt(dtDict:dict):
  '''convert unjsonable datetime object to timestamp in the dictionary'''
  from datetime import datetime
  return {k: (filterDt(v) if type(v) == dict else v) if type(v) != datetime else v.timestamp()
            for k,v in dtDict.items()}

# Cell
def stripDict(data:dict):
  return {k: v.strip() if type(v) == str else v for k,v in data.items()}

# Cell
import hashlib, pickle, base64
def hashDict(data:dict, hasher= hashlib.sha1(), encoder = pickle.dumps):
  hasher.update(encoder(data))
  rawHash = hasher.digest()
  return base64.b64encode(rawHash).decode()

# Cell
import pickle
def saveDictToFile(data:dict, path:str):
  with open(path, 'wb')as f:
    pickle.dump(data,f,protocol=pickle.HIGHEST_PROTOCOL)

def loadDictFromFile(path:str):
  with open(path, 'rb') as f:
    return pickle.load(f)

# Cell
def saveStringToFile(data:str, path:str):
  with open(path, 'w')as f:
    f.write(data)
def loadStringFromFile(path:str):
  with open(path, 'r')as f:
    return f.read()

# Cell
def genSchema(inputDict:dict, format_='yaml')->(dict,str):
  '''generate a json schema from dict,
  format::str:
    default='yaml', return schema in json or yaml
    'json', return the json schema
  response
    'both', return a tuple of (json, yaml)
    dict or string
  '''
  from genson import SchemaBuilder
  import yaml
  builder = SchemaBuilder()
  builder.add_object(inputDict)
  schema = builder.to_schema()
  if format_=='yaml':
    return yaml.dump(schema)
  elif format_ == 'json':
    return schema
  elif format_ == 'both':
    return schema, yaml.dump(schema)
  else:
    return schema, yaml.dump(schema)