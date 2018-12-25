#找标题
def findName(title):
    return str(title).replace("<div class=\"caption\">","").replace("</div>","")

def findImgUrl(imgUrl):

    start = str(imgUrl).find("data-src=\"https://t.nhentai.net/galleries/")
    if (start != -1):
        end1 = str(imgUrl).find("/thumb.jpg")
        if (end1 == -1):
            end2 = str(imgUrl).find("/thumb.png")
            if (end2 != -1):
                return str(imgUrl)[start + 10:end2 + 10]
        else:
            return str(imgUrl)[start + 10:end1 + 10]
#找到图片
def findAllImg(ImgsUrl):
    s=""
    start = ImgsUrl.find("<a class=\"cover\" href=\"")
    if (start != -1):
        end = ImgsUrl.find("\" style=\"padding:0 0")
        if (end != -1):
            s=ImgsUrl[23:end]
            return s

#找到资源ID
def finimgid(html):
    mstart = str(html).find(",\"media_id\":\"")
    mend = str(html).find("\",\"title\"")
    return str(html)[mstart+13:mend]
#找到页数
def getpagenumber(html):
    start = str(html).find(",\"num_pages\":")
    end = str(html).find(",\"num_favorites\"")
    return str(html)[start+13:end]
