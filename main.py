from bs4 import BeautifulSoup
import requests
import os
import json
import time
import sys


def showMsg(msg):
    print('[' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + '] ' + msg)


def downloadGallery(content_html):
    global headers
    if not content_html.find('h1'):
        showMsg("该图集访问失败，已跳过！\n")
        return
    name_ja = content_html.find('h1').get_text().replace('?', '？').replace(':', '：').replace('/', ' ').replace('|', '、').replace('*', '·').replace('"', '\'').replace('<', '《').replace('>', '》').replace("...", "").replace('\t', ' ').replace('\n', ' ').replace('\\', ' ').strip('.').strip()
    if not os.path.exists(os.path.join('Gallery', name_ja)):
        os.mkdir(os.path.join('Gallery', name_ja))
    else:
        showMsg("该图集已下载，正在检查文件完整性...")
    name_en = content_html.find('h2').get_text().replace('?', '？').replace(':', '：').replace('/', ' ').replace('|', '、').replace('*', '·').replace('"', '\'').replace('<', '《').replace('>', '》').replace("...", "").replace('\t', ' ').replace('\n', ' ').replace('\\', ' ').strip('.').strip()
    raw_tags = content_html.find(class_='listdetail_box ldb1').find_all('div')[-1].find_all('a')
    tags = []
    img_links = []
    failed_links = []
    for raw_tag in raw_tags:
        tags.append(raw_tag.get_text())
    for img_html in content_html.find_all(class_='vimg lazyload'):
        img_links.append(img_html.get('data-src'))
    json_path = os.path.join('Gallery', name_ja, 'meta.json')
    if not os.path.exists(json_path):
        showMsg("Downloading Meta Data ...")
        with open(json_path, 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps({'name_ja': name_ja, 'name_en': name_en, 'tags': tags, 'links': img_links},
                                       ensure_ascii=False))
    for img_link in img_links:
        img_name = img_link.split('/')[-1]
        img_path = os.path.join('Gallery', name_ja, img_name)
        if not os.path.exists(img_path):
            img_data_raw = requests.get(img_link, headers=headers)
            img_data = img_data_raw.content
            if img_data_raw.status_code == 200:
                showMsg("Download Image: [" + img_name + "] Success !")
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
            elif img_data_raw.status_code == 404:
                if img_link.endswith('jpg'):
                    img_link = img_link.replace('jpg', 'png')
                else:
                    img_link = img_link.replace('png', 'jpg')
                img_data_raw = requests.get(img_link, headers=headers)
                img_data = img_data_raw.content
                if img_data_raw.status_code == 200:
                    showMsg("Download Image: [" + img_name + "] Success !")
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)
                elif img_data_raw.status_code == 400:
                    showMsg("Image Lost: " + img_name)
                else:
                    showMsg("Download Failed: " + img_link)
                    failed_links.append(img_link)
            else:
                showMsg("Download Failed: " + img_link)
                failed_links.append(img_link)
        else:
            showMsg("Image [" + img_name + "] Already Exists.")
    if len(failed_links) == 0:
        showMsg("当前图集所有文件下载完成！\n")
    else:
        showMsg("当前图集下载异常，共 " + str(len(failed_links)) + "个文件下载失败：")
        for failed_link in failed_links:
            print(failed_link)
        print("")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

if not os.path.exists('Gallery'):
    os.mkdir('Gallery')

if len(sys.argv) > 1:
    input_link = sys.argv[1]
else:
    input_link = input("请输入下载链接：")

page_num = 1

if "detail" in input_link:  # 如果是漫画详情页，则遍历下载每张图片
    try:
        content = requests.get(input_link, headers=headers)
        content_html = BeautifulSoup(content.text, 'lxml')
    except:
        print("\n获取网页原始信息错误！\n")
        sys.exit()
    downloadGallery(content_html)
else:  # 如果是搜索结果列表页，则先进入详情页再下载
    if not "page" in input_link:
        input_link = os.path.join(input_link, "page/1")
    else:
        page_num = int(input_link.split('/')[-1])
    while True:
        input_link = os.path.join(os.path.dirname(input_link), str(page_num)).replace("\\", "/")
        try:
            content = requests.get(input_link, headers=headers)
            content_html = BeautifulSoup(content.text, 'lxml')
        except:
            print("\n获取网页原始信息错误！\n")
            sys.exit()
        showMsg("-------------------------------------------------------------")
        showMsg("正在开始下载列表页：" + input_link)
        showMsg("-------------------------------------------------------------")
        for gallery_html in content_html.find_all('a', class_='list-wrap gallery'):
            gallery_link = "https://zha.erocool.me" + gallery_html.get('href')
            gallery_name = gallery_html.find('h3', class_='caption').get('title')
            showMsg("Start Download: [" + gallery_name + "]")
            try:
                detail = requests.get(gallery_link, headers=headers)
                detail_html = BeautifulSoup(detail.text, 'lxml')
            except:
                print("\n获取详情页原始信息错误！\nError Detail Page Link: [" + gallery_link + "]\n")
                continue
            downloadGallery(detail_html)
        page_num = page_num + 1


    

    
    