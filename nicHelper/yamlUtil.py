# AUTOGENERATED! DO NOT EDIT! File to edit: yaml.ipynb (unless otherwise specified).

__all__ = ['loadYamlUrl']

# Cell
from beartype import beartype
import yaml, requests

# Cell
def loadYamlUrl(url:str, headers:dict = {}, loader=yaml.FullLoader)->dict:
  '''
    load yaml from url as a dictionary for example:
      testUrl = 'https://raw.githubusercontent.com/thanakijwanavit/villaMasterSchema/dev/coupon/testData/buyXGetY.yaml'
      loadYamlUrl(testUrl)
    input:
      url:str: url of the file
      headers:Optional[dict]:headers
      loader:yaml.Loader: optional yaml loader default is yaml.FullLoader
    response:
      dict: yaml load of the file
  '''
  r = requests.get(url, headers=headers).content
  return yaml.load(r, Loader = loader)
