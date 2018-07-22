import requests
from bs4 import BeautifulSoup
import re

header = {"Referer": "http://img.mmjpg.com/","User-Agent": "Mozilla/5.0"}

def GetSetAmount():
    homepage = 'http://www.mmjpg.com/'
    r_homepage = requests.get(homepage, headers = header)
    if r_homepage.status_code == 200:
        print('当前网页访问正常')
    r_homepage.encoding = r_homepage.apparent_encoding
    html_homepage = r_homepage.text
    soup_homepage = BeautifulSoup(html_homepage, 'html.parser')
#    print(homepage_soup.img)
    LatestImg_url = soup_homepage.img.attrs['src']
#    print(LatestImg_url)
#    print(type(LatestImg_url))
    print('网站当前共有：', LatestImg_url[-8:-4], '个图片集')
    SetAmount = LatestImg_url[-8:-4]
    return SetAmount

'''根据url规律，生成每个图集的url，用yield关键字得到一个图集url生成器'''
def GetPicSet_url():
    setamount = int(GetSetAmount())
    global Set_n
    for Set_n in range(1, setamount+1):
        yield 'http://www.mmjpg.com/mm/' + str(Set_n)  

'''获取每个图集的图片数量'''
def GetPicAmount_EverySet(PicSet_url):
    r_set = requests.get(PicSet_url, headers = header)
    r_set.encoding = r_set.apparent_encoding
    html_set = r_set.text
    soup_set = BeautifulSoup(html_set, 'html.parser')
    tag_pagenumber = soup_set.find_all(href = re.compile('^/mm/'))
    tag_lastpage = tag_pagenumber[6]
    PicAmount = tag_lastpage.string
    return PicAmount

'''获取每张图片的url'''
def GetImg_url(Pic_url):
    r_pic = requests.get(Pic_url, headers = header)
    r_pic.encoding = r_pic.apparent_encoding
    html_pic = r_pic.text
    soup_pic = BeautifulSoup(html_pic,'html.parser')
    global set_name
    set_name = soup_pic.h2.string
    imgTag = soup_pic.find('img')
    Img_url = imgTag.attrs['src']
    return Img_url

'''保存图片'''
def GetJpg():
    for PicSet_url in GetPicSet_url():
        global Set_n
        maxpage_Set = int(GetPicAmount_EverySet(PicSet_url))
        for pagenumber in range (1, maxpage_Set + 1):
            PicWeb_url = 'http://www.mmjpg.com/mm/' + str(Set_n) + '/' + str(pagenumber)
            Img_url = GetImg_url(PicWeb_url)
            content = requests.get(Img_url, headers = header).content
            global set_name
            Pic_name = r'C:\Users\Andy Hu\Desktop\MM\\' + set_name + str(pagenumber) +'.jpg'
            #文件名中的\U开始的字符被编译器认为是八进制,要加r标识,最后一个\要加一个\转义
            with open(Pic_name, 'wb') as f: 
                f.write(content) 
            print('已经保存第', Set_n, '个图集的第', pagenumber, '张图片')

GetJpg()