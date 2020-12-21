# AUTOGENERATED! DO NOT EDIT! File to edit: pdUtils.ipynb (unless otherwise specified).

__all__ = ['getDfHash', 'saveLocalCache', 'saveLocalHash', 'loadLocalCache', 'loadLocalHash', 'saveRemoteHash',
           'saveRemoteCache', 'loadRemoteCache', 'loadRemoteHash']

# Cell
import pandas as pd
from hashlib import sha1
from .dictUtil import saveStringToFile, loadStringFromFile
from s3bz.s3bz import S3
import os

# Cell
def getDfHash(df:pd.DataFrame):
  df.to_feather('/tmp/feather')
  with open('/tmp/feather', 'rb') as f:
    objHash = sha1(f.read()).hexdigest()
  return objHash

# Cell
def saveLocalCache( data:pd.DataFrame, path = '/tmp/cache'):
  saveLocalHash(data, path=path)
  return data.to_feather(path)
def saveLocalHash( data:pd.DataFrame, path = '/tmp/hash'):
  dataHash = getDfHash(data)
  saveStringToFile(dataHash,path)
def loadLocalCache( path = '/tmp/cache'):
  if not os.path.exists(path): raise Exception('cache doesnt exist')
  return pd.read_feather(path)
def loadLocalHash( path = '/tmp/hash'):
  if not os.path.exists(path): raise Exception('hash doesnt exist')
  return loadStringFromFile(path)

# Cell
def saveRemoteHash(data:pd.DataFrame, key='', bucket='', **kwargs):
  hashKey = f'{key}-hash'
  hashString = getDfHash(data)
  dictToSave= {'hash': hashString }
  print(f'hashKey is {hashKey}')
  print('saving hash to s3')
  S3.save(key=hashKey,objectToSave=dictToSave, bucket=bucket, **kwargs )
  print(f'saved hash {hashString}')


def saveRemoteCache(data:pd.DataFrame, key = '',
                    bucket = '', localCachePath='/tmp/cache', localHashPath='/tmp/hash', **kwargs):

  saveLocalCache(data=data, path = localCachePath)
  saveLocalHash(data=data, path = localHashPath)
  saveRemoteHash(data=data, key = key, bucket=bucket)
  S3.saveFile(key=key, path=localCachePath, bucket=bucket, **kwargs)

def loadRemoteCache(key='', bucket='', **kwargs):
  path = '/tmp/tmpPath'
  S3.loadFile(key,path=path ,bucket=bucket, **kwargs)
  df = pd.read_feather(path)
  return df

def loadRemoteHash(key='', bucket='', **kwargs):
  hashKey = f'{key}-hash'
  print(f'loading hashkey {hashKey}')
  loadedHash= S3.load(hashKey,bucket=bucket, **kwargs).get('hash')
  print(f'loaded hash is {loadedHash}')
  return loadedHash