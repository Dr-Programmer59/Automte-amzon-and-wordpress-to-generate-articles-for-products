from tarfile import TarError
from bs4 import BeautifulSoup
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog,QApplication,QWidget
import threading
import requests
import json
import threading
import base64
import sys
from PIL import Image,ImageOps
import csv
import os
import random
import aiohttp
import asyncio
from PIL import ImageFont
from PIL import ImageDraw

Features=[[],[],[],[],[],[],[],[],[],[]]
prodID=[[],[],[],[],[],[],[],[],[],[]]
headers = {
        'authority': 'images-na.ssl-images-amazon.com',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': 'text/css,*/*;q=0.1',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'style',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }



async def get_page(session,url):
    async with session.get(url) as r:
        return await r.text()

async def get_all(session,urls):
    tasks=[]
    for url in urls:
        try:
            task=asyncio.create_task(get_page(session,"https://amazon.com/"+url))
            tasks.append(task)
        except: 
            continue
    result= await asyncio.gather(*tasks)
    return result
async def main(urls):
    async with aiohttp.ClientSession(headers=headers) as session:
        data=await get_all(session,urls)
        
        return data
def triplePICS(keyword,links,siteText):
    keyword=keyword.replace("+"," ")
    print(links)
    index=1
    for link in links:
        print("1")
        print(f"https://m.media-amazon.com/images/I/{link[0]}._SL500_.jpg")
        r = requests.get(f"https://m.media-amazon.com/images/I/{link[0]}._SL500_.jpg", allow_redirects=True)
        open(f'images/{keyword}{index}.jpg', 'wb').write(r.content)
        index+=1
    
    images = [Image.open(x) for x in [f'images/{keyword}1.jpg', f'images/{keyword}2.jpg', f'images/{keyword}3.jpg']]
    images[0]=images[0].resize((500,500))
    images[1]=images[1].resize((500,500))
    images[2]=images[2].resize((500,500))
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]
    I1 = ImageDraw.Draw(new_im)
    # Add Text to an image
    myFont = ImageFont.truetype("arial.ttf", 15, encoding="unic")
    I1.text((28, 28), siteText,font=myFont, fill=(0, 0,0))
    new_im = ImageOps.expand(new_im, border = 10, fill = 20)
    new_im.save(f'images/{keyword}.jpg')

def getArticles(link_arr,link_text,Feature,prodID,keyword,ref_code,imageBanner,paragraph1,paragraph2,paragraph3,prodsNum,btncolor):
    keyword=keyword.replace("+"," ")
    
    if("-" in prodsNum):
        prodNumStart=prodsNum.split("-",1)[0]
        prodNumEnd=prodsNum.split("-",1)[1]
    randomNumber=int(random.randint(int(prodNumStart),int(prodNumEnd)))
    f = open("index.html", "r",encoding="utf-8")
    textfile=f.readlines()
    disc=""
    for text in textfile:
        disc+=text
    return disc.format(
    link1_text=link_text[0].replace("+"," "),link1="https://www.amazon.com/dp/"+link_arr[0].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link2_text=link_text[1].replace("+"," "),link2="https://www.amazon.com/dp/"+link_arr[1].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link3_text=link_text[2].replace("+"," "),link3="https://www.amazon.com/dp/"+link_arr[2].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link4_text=link_text[3].replace("+"," "),link4="https://www.amazon.com/dp/"+link_arr[3].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link5_text=link_text[4].replace("+"," "),link5="https://www.amazon.com/dp/"+link_arr[4].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link6_text=link_text[5].replace("+"," "),link6="https://www.amazon.com/dp/"+link_arr[5].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link7_text=link_text[6].replace("+"," "),link7="https://www.amazon.com/dp/"+link_arr[6].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link8_text=link_text[7].replace("+"," "),link8="https://www.amazon.com/dp/"+link_arr[7].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link9_text=link_text[8].replace("+"," "),link9="https://www.amazon.com/dp/"+link_arr[8].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link10_text=link_text[9].replace("+"," "),link10="https://www.amazon.com/dp/"+link_arr[9].split("/dp/",1)[1].split("ref",1)[0]+f"?tag={ref_code}",
    link1_F=Feature[0][0],
    prodID_1=prodID[0][0],
    link2_F=Feature[1][0],
    prodID_2=prodID[1][0],
    link3_F=Feature[2][0],
    prodID_3=prodID[2][0],
    link4_F=Feature[3][0],
    prodID_4=prodID[3][0],
    link5_F=Feature[4][0],
    prodID_5=prodID[4][0],
    link6_F=Feature[5][0],
    prodID_6=prodID[5][0],
    link7_F=Feature[6][0],
    prodID_7=prodID[6][0],
    link8_F=Feature[7][0],
    prodID_8=prodID[7][0],
    link9_F=Feature[8][0],
    prodID_9=prodID[8][0],
    link10_F=Feature[9][0],
    prodID_10=prodID[9][0],
    keyword=keyword,
    imageBanner=imageBanner,
    paragraph1=paragraph1.format(prodNum=randomNumber,keyword=keyword),
    paragraph2=paragraph2.format(prodNum=randomNumber,keyword=keyword),
    paragraph3=paragraph3.format(prodNum=randomNumber,keyword=keyword),
    buttoncolor=btncolor,



    )
def FeatureFetcher(content,index):
            global prodID,Features,threading_count
            feature_str=""
            prodContent=BeautifulSoup(content,"html.parser")
            prodID[index].append(prodContent.find("div",{"id":'imgTagWrapperId'}).find("img")['src'].split("/images/I/",1)[1].split(".",1)[0])
            print(prodContent.find("div",{"id":'imgTagWrapperId'}).find("img")['src'].split("/images/I/",1)[1].split(".",1)[0])
            qualities=prodContent.find("div",{"id":"feature-bullets"}).find_all("li")
            color=['red','green']
            color_index=0
            for x in qualities:
                feature_str+=f"<li><i class='fas fa-check' style='color:{color[color_index]}'></i>"+str(x.get_text())+"</li>"
                if color_index==0:
                    color_index+=1
                else:
                    color_index=0
                
            Features[index].append(feature_str)
            print(feature_str)
           
         

      
        
    
def scrapeData(url):
    
    params = (
        ('AUIClients/DramAssets', ''),
    )

    response = requests.get(url, headers=headers, params=params)
    from bs4 import BeautifulSoup
    content=BeautifulSoup(response.content,"html.parser")
    return content





def search(keywords_path,prefix,sufix,ref_code,progressBar,prodsNum,wp_admin,wp_pass,wp_url,category_name,tags,status_post,btncolor,siteText):
    if(btncolor==""):
        btncolor="#f9a711"    
    paragraph1_path=os.listdir(os.getcwd()+"/paragraph1")
    paragraph2_path=os.listdir(os.getcwd()+"/paragraph2")
    paragraph3_path=os.listdir(os.getcwd()+"/paragraph3")
    with open("paragraph1/"+random.choice(paragraph1_path),"r",encoding="utf-8") as f:
        paragraph1=f.read()
    with open("paragraph2/"+random.choice(paragraph2_path),"r",encoding="utf-8") as f:
        paragraph2=f.read()
    with open("paragraph3/"+random.choice(paragraph3_path),"r",encoding="utf-8") as f:
        paragraph3=f.read()
    keywords=[]
    with open(keywords_path,"r",encoding="utf-8") as f:
        csvwriter = csv.reader(f)
        for i in csvwriter:
            keywords.append(i)
    for keyword in keywords:
        try:
            global prodID,Features
            Features=[[],[],[],[],[],[],[],[],[],[]]
            prodID=[[],[],[],[],[],[],[],[],[],[]]
            links=[]
            link_text=[]
            keyword=keyword[0].replace(" ","+")
            url=f"https://www.amazon.com/s?k={keyword}"
            amazonContent=scrapeData(url)
            title_Prod=amazonContent.find_all("div",class_="s-title-instructions-style")
            index=0
            number=0
            progressBar.setText("Checking for top 10 products")
            while(number<10):
                if("Sponsored" not in title_Prod[index].get_text() and "Featured from our brands" not in title_Prod[index].get_text() and "Prime Video" not in title_Prod[index].get_text()):
                    print(title_Prod[index].find("a")['href'])
                    links.append(title_Prod[index].find("a")['href'])
                    link_text.append(title_Prod[index].find("a").get_text().split(",",1)[0])
                    number+=1
                index+=1
            index=0
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            htmls= asyncio.run(main(links))
            index=0
            for html in htmls:
                progressBar.setText(f"Working on Link-{index+1}")
                FeatureFetcher(html,index)
                index+=1
            print(Features)
            print(prodID)
            triplePICS(keyword,prodID[:3],siteText) 
        
            categories_array=category_name.split("+")
            tags_array=tags.split("+")
            
            
            if True:
                    user = wp_admin
                    pythonapp = wp_pass
                    if(str(wp_url).endswith("/")):
                        wp_url=wp_url[:len(wp_url)-1]
                    url = wp_url+'/wp-json/wp/v2'
                    token = base64.b64encode((user + ':' + pythonapp).encode())
                    headers = {'Authorization': 'Basic ' +token.decode('utf-8')}
                    #Code for the categories
                    id_category=[]
                    id_tags=[]
                    print(categories_array)
                    for category_ in categories_array:
                            post={
                                "name":category_
                            }
                            responce = requests.post(url +"/categories", headers=headers, json=post)
                            print(responce.json())
                            try:
                                id_category.append(int(json.loads(responce.content)['id']))
                            except:
                                id_category.append(int(json.loads(responce.content)['data']['term_id']))
                    for tag in tags_array:
                            post={
                                "name":tag
                            }
                            responce = requests.post(url +"/tags", headers=headers, json=post)
                            print(responce.json())
                            try:
                                id_tags.append(int(json.loads(responce.content)['id']))
                            except:
                                id_tags.append(int(json.loads(responce.content)['data']['term_id']))

                    

                    title=keyword.replace("+"," ")
                    #Code for the media uploading
                    media={
                        'file':open(f"images/{title}.jpg",'rb'),
                        'caption':prefix+" "+keyword+" "+sufix,
                        'discription':prefix+" "+keyword+" "+sufix
                    }
                    image=requests.post(url+"/media",headers=headers,files=media)
                    imageBanner=str(json.loads(image.content)['source_url'])

                    article=getArticles(links,link_text,Features,prodID,keyword,ref_code,imageBanner,paragraph1,paragraph2,paragraph3,prodsNum,btncolor)
                    #codee for posting the article
                    
                    post={
                        "title":f"{prefix} {title} {sufix}",
                        "content":article, 
                        "status":status_post, 
                        "categories":id_category,
                        "tags":id_tags
                        
                    }

            r=requests.post(url+"/posts",headers=headers,json=post)
            
            os.remove(f"images/{title}1.jpg")
            os.remove(f"images/{title}2.jpg")
            os.remove(f"images/{title}3.jpg")
            
            progressBar.setText(f"The {title} has been posted with status code [{r}]")
        except:
            progressBar.setText(f"The {title} has been posted with status code [404]")


            










class MainScreen(QDialog):
    def __init__(self):
        super(MainScreen, self).__init__()
        loadUi("main.ui",self)
        self.start.clicked.connect(self.process)

    def process(self):
        t = threading.Thread(target=lambda:search(self.keywords.text(),str(self.prefix.text()),str(self.sufix.text()),str(self.ref_code.text()),self.progressBar,str(self.prodsNum.text()),str(self.wordpressAdmin.text()),str(self.wordpressPass.text()),str(self.wordpressUrl.text()),str(self.category.text()),str(self.tags.text()),str(self.status_category.currentText()),str(self.btn_color.text()),str(self.siteText.text())))
        t.daemon=True
        t.start()

app=QApplication(sys.argv)
welcome=MainScreen()
widget= QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(800)
widget.setFixedHeight(500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('exiting')
    