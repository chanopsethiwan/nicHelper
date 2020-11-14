# Helpers
> various helpers from nic gist


```
from nicHelper.wrappers import add_method
```

## Install

`pip install nicHelper`

# How to use

### method module

### add method to a class

```
class A:
  pass
@add_method(A)
def printHello(self):
  print('hello')

A().printHello()
```

    hello


## Dict utilities

```
from nicHelper.dictUtil import printDict
printDict({'key':'sjfhdkljhafsdlkjhdfaslkjhkljfadshklhfa', 'nestedKey':{'nestedKey2':'938023840843', 'nested3':{'nested4':'hello'}}})
```

    key : sjfhdkljha
    nestedKey
     nestedKey2 : 9380238408
     nested3
      nested4 : hello


## Exception module

```
from nicHelper.exception import errorString
try:
  error
except:
  print(f'error is \n{errorString()}')
```

    error is 
    Traceback (most recent call last):
      File "<ipython-input-5-86083feec525>", line 3, in <module>
        error
    NameError: name 'error' is not defined
    


## Image utils

```
from nicHelper.images import imageFromUrl, imageToS3, showImgS3, resizeImage
from s3bz.s3bz import S3
```

```
## test variables
key = 'testCat.png'
path = '/tmp/testCat.png'
bucket = 'villa-remove-bg-small-output'
url = 'https://sites.google.com/site/funnycatmeawww/_/rsrc/1422326075261/home/6997052-funny-cat.jpg?height=675&width=1200'
```

### Resize images

```
resizeImage(url, 400)
```




![png](docs/images/output_15_0.png)



### load image from url

```
img = imageFromUrl(url)
type(img)
```




    PIL.JpegImagePlugin.JpegImageFile



### save Image to S3

```
imageToS3(img, bucket, key)
S3.exist(key,bucket)
```

    saving image to villa-remove-bg-small-output/testCat.png





    True



### display image from s3

```
## full test
showImgS3(bucket, key)
```


![png](docs/images/output_21_0.png)

