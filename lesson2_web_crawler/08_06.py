#%%
import requests
from requests.api import patch

r=requests.get("http://www.google.com")
if r.status_code==200:
    print("請求成功")
    print(r.text)
else:
    print("請求失敗")


#%%%
# httpbin,httpbin/get,httpbin/post
import requests
url_pa={'name':'chiu','score':99,"name1":"邱"}
r=requests.get("http://www.yahoo.co.jp",params=url_pa)
print(r.url)


# 解碼用url decode

#%%
import requests
url_data={'name':'邱老師','score':99}
r=requests.post('http://www.httpbin.org/post',data=url_data)
print(r.url)
print(r.text)

# delete  get  patch post put  (http methods)

print(r.encoding)
#%%
import requests
r=requests.get('http://www.google.com')
print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])
print(r.request.headers)
print(r.status_code)


# %%
kv={'User-Agent':'Mozilla/5.0'}
r1=requests.get('http://www.amazon.com',headers=kv)
r1.request.headers
print(r1.status_code)
print(r1.text)

# %%


# %%



# %%



# %%



# %%



# %%



# %%



# %%


