import os
import requests
from bs4 import BeautifulSoup

def get_urls(url):
    video_urls = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a')
    next_page_flag, next_page_url = False, ''
    for item in results:
        url_href = item.get('href')
        title = item.get('title')
        content = item.text
        full_url = 'https:' + url_href

        # if url is a video add it to video_urls list.
        if url_href.startswith('//v.youku.com/v_show/id_'):
            video_urls.append('{};{}'.format(full_url, title))
            print('{};{}'.format(full_url, title))

        # if encounter '下一页' recusive call get_urls
        if content == '下一页':
            next_page_url = full_url
            next_page_flag = True

    if not next_page_flag:
        return video_urls
    else:
        video_urls.extend(get_urls(full_url))
        return video_urls



if __name__ == '__main__':
    url = 'https://list.youku.com/category/show/c_97.html?spm=a2hcb.12701310.app.5~5!2~5!2~5~5~DL~DD~A' #优酷电视剧列表页
    video_urls = get_urls(url)

