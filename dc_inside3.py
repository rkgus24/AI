import time
import requests, re
from bs4 import BeautifulSoup
from IPython.core.display import display, HTML
 
#봇 차단을 위한 헤더 설정
headers = {
    "Connection" : "keep-alive",
    "Cache-Control" : "max-age=0",
    "sec-ch-ua-mobile" : "?0",
    "DNT" : "1",
    "Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site" : "none",
    "Sec-Fetch-Mode" : "navigate",
    "Sec-Fetch-User" : "?1",
    "Sec-Fetch-Dest" : "document",
    "Accept-Encoding" : "gzip, deflate, br",
    "Accept-Language" : "ko-KR,ko;q=0.9"
    }
 
#갤러리 타입 가져오기(마이너, 일반)
def get_gallary_type(dc_id):
    #url로 requests를 보내서 redirect시키는지 체크한다.
    url = f'https://gall.dcinside.com/mgallery/board/lists/?id={dc_id}'
    
    result = url
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    if "location.replace" in str(soup):
        redirect_url = str(soup).split('"')[3]
        result = redirect_url
    if "mgallery" in result:
        result = "mgallery/board"
    else:
        result = "board"
        
    return result
 
#글 파싱 함수
def article_parse(dc_id, keyword):
    g_type = get_gallary_type(dc_id)
    url = f"https://gall.dcinside.com/{g_type}/lists/?id={dc_id}&page=1&s_type=search_subject_memo&s_keyword={keyword}"
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
 
    article_list = soup.select(".us-post") #글 박스 전부 select
    for element in article_list:
        #글 박스를 하나씩 반복하면서 정보 추출
        link = "https://gall.dcinside.com/" + element.select("a")[0]['href'].strip()
        num = element.select(".gall_num")[0].text
        title = element.select(".ub-word > a")[0].text
        reply = element.select(".ub-word > a.reply_numbox > .reply_num")
        if reply : reply = reply[0].text
        else : reply = ""
        nickname = element.select(".ub-writer")[0].text.strip()
        timestamp = element.select(".gall_date")[0].text
        refresh = element.select(".gall_count")[0].text
        recommend = element.select(".gall_recommend")[0].text
 
        print(link, num, title, reply, nickname, timestamp, refresh, recommend)
        display(HTML(f'{num} <a href = "{link}" target="_blank">{title}</a> {reply} {nickname} {timestamp} {refresh} {recommend}'))
    
 
#검색할때 설정해줘야할 것들
dc_id = "bssm"
keyword = "게이"
 
article_parse(dc_id, keyword)