import requests
import pandas

url="https://fakestoreapi.com/products"

req=requests.get(url)
data=req.json()
#print(data)

"""for i in data:
    print(i)"""

#pd=pandas.DataFrame(data)
pd=pandas.json_normalize(data)
print(pd)
