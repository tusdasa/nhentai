from net.tusdasa.sp import Start
import time
# nhentai 爬虫 此处控制页数
Url = "https://nhentai.net/?page="

for i in range(1,11):
    Start.start(Url+str(i))
    time.sleep(5)