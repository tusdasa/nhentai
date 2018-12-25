from net.tusdasa.sp import Download
from net.tusdasa.sp import FindName
from net.tusdasa.sp import SafeFileName
from urllib import request
from bs4 import BeautifulSoup
import time

def start(Url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }

    req = request.Request(Url, headers=headers)

    resp = request.urlopen(req)

    html = resp.read().decode()
    soup = BeautifulSoup(html, "html5lib")

    atag = soup.find_all('a')
    divtag = soup.find_all('div')


    info = []
    title = []
    f = open('list.text','a',encoding='UTF-8')
    for i in range(0,len(atag)):
        if( i >= 17 and i <= 41 ):
            temp = "https://nhentai.net"+FindName.findAllImg(str(atag[i]))
            info.append(temp)
            print(temp)


    for i in range(4,len(divtag)):
        if (i % 2 != 0):
            tit = FindName.findName(str(divtag[i]))
            title.append(tit)
            print(tit)
            f.write(tit+"\n")

    f.close()

    pages =[]
    imgs = []

    for i in range(len(info)):
        req = request.Request(str(info[i]), headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode()
        temp = FindName.getpagenumber(html)
        pages.append(temp)
        print("page= "+temp)
        temp1 = "https://i.nhentai.net/galleries/"+FindName.finimgid(html)+"/"
        imgs.append(temp1)
        print("imgs= "+temp1)
        time.sleep(2)

    #print(pages)
    #print(imgs)

    for i in range(len(pages)):
        SafeFileName.safename(str(title[i]))
        for j in range(1, int(pages[i])+1):
            t1 = SafeFileName.safeimg(str(title[i]), str(j))
            t2 = imgs[i]+str(j)+".jpg"
            print("Start Download " + t2)
            try:
                Download.downloadFile(t1, t2)
                print("Download Success")
            except:
                t2 = imgs[i] + str(j) + ".png"
                Download.downloadFile(t1,t2)
                print("Download Success")

            print(t1)

            time.sleep(2)