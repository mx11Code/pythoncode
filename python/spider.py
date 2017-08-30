import os
import requests
from lxml import html

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    # 'pragma': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}


def save(text, filename='temp', path=r'C:\Users\Administrator\Desktop\spider'):
    fpath = os.path.join(path, filename)
    with open(fpath, 'wb+') as f:
        f.write(text)


def save_image(image_url):
    resp = requests.get(image_url)
    page = resp.content
    filename = image_url.split('zhimg.com/')[-1]
    print(image_url, filename)
    save(page, filename)


def crawl(zhihu_url):
    # resp = requests.get(url, headers=headers)
    # page = resp.content
    page = requests.get(url, headers=headers).content
    root = html.fromstring(page)
    image_urls = root.xpath('//img[@data-original]/@data-original')
    print('count', len(image_urls))
    # print(image_urls)
    for image_url in image_urls:
        # print(image_url)
        save_image(image_url)


if __name__ == '__main__':
    url = 'https://www.zhihu.com/question/23212066'
    crawl(url)
