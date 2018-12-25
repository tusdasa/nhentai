from urllib.request import urlretrieve
#下载工具
def downloadFile(filename,url):
    if(filename!=None and url!=None):
        urlretrieve(url, filename)
