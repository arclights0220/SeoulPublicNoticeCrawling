from asyncio import sleep
from asyncio.windows_events import NULL
from datetime import date, datetime
from ntpath import join
from posixpath import split, splitext
from re import search
from socket import TCP_NODELAY
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import html.parser
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import Select
import webbrowser
import warnings


warnings.filterwarnings(action='ignore')


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[
    0]  # 크롬드라이버 버전 확인
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
# 크롬드라이버 업데이트
try:
    driver = webdriver.Chrome(
        f'./{chrome_ver}/chromedriver.exe', chrome_options=options)
except:
    chromedriver_autoinstaller.install(cwd=True)
    driver = webdriver.Chrome(
        f'./{chrome_ver}/chromedriver.exe', chrome_options=options)


driver.execute_script("window.onbeforeunload = function() {};")


# 고시공고 검색 -> 차트의 가장 첫번째 결과 텍스트만 뽑기


def gangnam(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gangnam.go.kr/notice/list.do?mid=ID05_0402"
        driver.get(url)
        box = driver.find_element_by_id('keyword')
        btn = driver.find_element_by_class_name('btn-darkblue')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents-wrap > div > div.notice.board.list.clear-b > div > div:nth-child(1) > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n강남구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:2]
            print("\n강남구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n강남구청 오류")
        webbrowser.open(url)
        print("\n", url)


def gangdong(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gangdong.go.kr/web/newportal/notice/01"
        driver.get(url)
        box = driver.find_element_by_id('sv')
        btn = driver.find_element_by_class_name('blue-but-sub2')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content_focus > div.table01.table-warp > table > tbody > tr')
        if not search_result:
            print("\n강동구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n강동구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n강동구청 오류")
        webbrowser.open(url)
        print("\n", url)
# iframe


def gangbuk(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gangbuk.go.kr/www/contents.do?key=8065"
        driver.get(url)
        iframe = driver.find_element_by_tag_name("iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_id("temp")
        btn = driver.find_element_by_tag_name('a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(32) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6)')
        if not search_result:
            print("\n강북구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n강북구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n강북구청 오류")
        webbrowser.open(url)
        print("\n", url)
# 웹게시판 검색


def gangseo(a):
    try:
        driver.implicitly_wait(15)
        driver.maximize_window()
        url = "https://www.gangseo.seoul.kr/gs040301"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[2]/main/div[2]/div[1]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_xpath("/html/body/form/fieldset/input[1]")
        btn = driver.find_element_by_xpath('/html/body/form/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div.bbslist-designgroup > table > tbody > tr.firstline')
        search_result_two = soup.select_one(
            'body > form > div.bbslist-designgroup > table > tbody > tr:nth-child(1)'
        )

        if search_result:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            del splittext[-1:]
            print("\n강서구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
        else:
            onlytext = search_result_two.getText()
            splittext = onlytext.split()
            print("\n강서구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n강서구청 오류")
        webbrowser.open(url)
        print("\n" + url)


def gwanak(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gwanak.go.kr/site/gwanak/ex/bbs/List.do?cbIdx=289"
        driver.get(url)
        box = driver.find_element_by_id('searchKey')
        btn = driver.find_element_by_class_name('s-command')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#boardDivId > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n관악구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:2]
            del splittext[-1:]
            print("\n관악구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n관악구청 오류")
        webbrowser.open(url)
        print("\n", url)


def gwangjin(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gwangjin.go.kr/portal/bbs/B0000003/list.do?menuNo=200192"
        driver.get(url)
        box = driver.find_element_by_name('searchWrd')
        btn = driver.find_element_by_class_name('b-sh')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > div.table.m > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n광진구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:3]
            print("\n광진구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n광진구청 오류")
        webbrowser.open(url)
        print("\n", url)


def guro(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.guro.go.kr/www/selectBbsNttList.do?bbsNo=663&key=1791&"
        driver.get(url)
        box = driver.find_element_by_id('searchKrwd_search')
        btn = driver.find_element_by_class_name('p-button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#board > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n구로구청 " + a + "에 관한 최신공고 : 없음")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-2:]
            print("\n구로구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n구로구청 오류")
        webbrowser.open(url)
        print("\n", url)


def geumcheon(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.geumcheon.go.kr/portal/tblSeolGosiDetailList.do?key=294&rep=1"
        driver.get(url)
        box = driver.find_element_by_id('searchKrwd')
        btn = driver.find_element_by_class_name('p-button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > div > div > fieldset > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n금천구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n금천구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n금천구청 오류")
        webbrowser.open(url)
        print("\n", url)


def nowon(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.nowon.kr/www/user/bbs/BD_selectBbsList.do?q_bbsCode=1003&q_clCode=0"
        driver.get(url)
        box = driver.find_element_by_name('q_searchVal')
        btn = driver.find_element_by_class_name('btn-primary')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#printArea > div:nth-child(2) > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n노원구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-2:]
            print("\n노원구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n노원구청 오류")
        webbrowser.open(url)
        print("\n", url)


def dobong(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.dobong.go.kr/Contents.asp?code=10004825"
        driver.get(url)
        iframe = driver.find_element_by_id("contentFrm")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_id("temp")
        btn = driver.find_element_by_tag_name('a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(32) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6)')
        if not search_result:
            print("\n도봉구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n도봉구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n도봉구청 오류")
        webbrowser.open(url)
        print("\n", url)


def ddm(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.ddm.go.kr/www/contents.do?key=201&searchNotAncmtSeCode=01,02,04,05,06,07"
        driver.get(url)
        iframe = driver.find_element_by_id("mergerFrame")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_id("temp")
        btn = driver.find_element_by_tag_name('a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > table:nth-child(32) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6)')
        if not search_result:
            print("\n동대문구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-1:]
            print("\n동대문구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                             for _ in splittext))
    except:
        print("\n동대문구청 오류")
        webbrowser.open(url)
        print("\n", url)


def dongjak(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.dongjak.go.kr/portal/bbs/B0000172/list.do?menuNo=200644"
        driver.get(url)
        box = driver.find_element_by_id('searchWrd')
        btn = driver.find_element_by_class_name('b-sh')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > div.clearfix > div.contentData > div.bdList > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n동작구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-1:]
            print("\n동작구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n동작구청 오류")
        webbrowser.open(url)
        print("\n", url)


def mapo(a):
    try:
        driver.implicitly_wait(30)
        url = "https://www.mapo.go.kr/site/main/home"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/input')
        btn = driver.find_element_by_xpath(
            '/html/body/div[2]/div[2]/div[2]/div/div[3]/div[2]/a[2]')
        box.send_keys(a)
        btn.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(5)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#boardSearch > div.inner_box > ul > li:nth-child(1) > div.top')
        if not search_result:
            print("\n마포구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[-2:]
            print("\n마포구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
            print("현재 마포구청은 코드 수정 중에 있습니다. 열리는 사이트에서 재검색해주십시오")
            webbrowser.open(url)
    except:
        print("\n마포구청 오류")
        webbrowser.open(url)
        print("\n", url)


def sdm(a):
    try:
        driver.implicitly_wait(15)

        url = "http://www.sdm.go.kr/news/notice/notice.do"
        driver.get(url)
        box = driver.find_element_by_id('keyword')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div[1]/ul/li[5]/a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#frm > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n서대문구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-2:]
            print("\n서대문구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                             for _ in splittext))
    except:
        print("\n서대문구청 오류")
        webbrowser.open(url)
        print("\n", url)


def seocho(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.seocho.go.kr/site/seocho/05/10506020000002015070811.jsp"
        driver.get(url)
        iframe = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div[2]/div[2]/div[2]/iframe")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_id("temp")
        btn = driver.find_element_by_class_name('btn_inline')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > form > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n서초구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-1:]
            print("\n서초구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n서초구청 오류")
        webbrowser.open(url)
        print("\n", url)


def sd(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.sd.go.kr/main/selectBbsNttList.do?key=1473&bbsNo=184&integrDeptCode=&searchCtgry=&searchCnd=SJ&searchKrwd="
        driver.get(url)
        box = driver.find_element_by_id('searchKrwd_search')
        btn = driver.find_element_by_class_name('p-button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#board > div > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n성동구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-2:]
            print("\n성동구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n성동구청 오류")
        webbrowser.open(url)
        print("\n", url)


def sb(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.sb.go.kr/main/cop/bbs/gosi.do"
        driver.get(url)
        box = driver.find_element_by_id('searchWord')
        btn = driver.find_element_by_xpath(
            '/html/body/div[3]/div/section/div/article/form/fieldset/input[2]')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#mainCont > form > div.bbsList > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n성북구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-1:]
            print("\n성북구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n성북구청 오류")
        webbrowser.open(url)
        print("\n", url)


def songpa(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.songpa.go.kr/www/selectGosiList.do?key=2776&not_ancmt_se_code="
        driver.get(url)
        box = driver.find_element_by_id('ipt_lab')
        btn = driver.find_element_by_class_name("p-button")
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n송파구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            del splittext[-3:]
            print("\n송파구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n송파구청 오류")
        webbrowser.open(url)
        print("\n", url)


def yangcheon(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.yangcheon.go.kr/site/yangcheon/ex/externalLinks/announcementList.do"
        driver.get(url)
        iframe = driver.find_element_by_id("mergerFrame")
        driver.switch_to.frame(iframe)
        box = driver.find_element_by_name("temp")
        btn = driver.find_element_by_tag_name('a')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > div.board_list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n양천구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:5]
            print("\n양천구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n양천구청 오류")
        webbrowser.open(url)
        print("\n", url)


def ydp(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.ydp.go.kr/www/selectEminwonList.do?not_ancmt_se_code=01%2C02%2C04%2C05%2C06%2C07&ofr_pageSize=10&key=2852&"
        driver.get(url)
        box = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/main/article/div/div[2]/form/fieldset/div/div/input")
        btn = driver.find_element_by_xpath(
            "/html/body/div[2]/div[2]/div/main/article/div/div[2]/form/fieldset/div/div/span[2]/button")
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div.p-wrap.bbs.bbs__list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n영등포구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n영등포구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                             for _ in splittext))
    except:
        print("\n영등포구청 오류")
        webbrowser.open(url)
        print("\n", url)
#전체 -> 제목


def yongsan(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.yongsan.go.kr/portal/bbs/B0000095/list.do?menuNo=200233"
        driver.get(url)
        box = driver.find_element_by_id('searchWrd')
        btn = driver.find_element_by_class_name("b-sh")
        select = Select(driver.find_element_by_name('searchCnd'))
        select.select_by_visible_text('제목')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > div.bd-list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n용산구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:2]
            del splittext[-1:]
            print("\n용산구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n용산구청 오류")
        webbrowser.open(url)
        print("\n", url)


def ep(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.ep.go.kr/www/selectEminwonList.do?key=754&notAncmtSeCode=01"
        driver.get(url)
        box = driver.find_element_by_xpath(
            "/html/body/div/div/div/main/article/div/div[1]/form/div/div[2]/input")
        btn = driver.find_element_by_xpath(
            '/html/body/div/div/div/main/article/div/div[1]/form/div/div[2]/button')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#contents > div.epform.bbs.gosi.list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n은평구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            print("\n은평구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n은평구청 오류")
        webbrowser.open(url)
        print("\n", url)


def jongno(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.jongno.go.kr/portal/bbs/selectBoardList.do?bbsId=BBSMSTR_000000000271&menuId=1756&menuNo=1756"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/fieldset/div/div/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[2]/div/div[2]/form/fieldset/div/div/input[2]')
        select = Select(driver.find_element_by_name('searchCnd'))
        select.select_by_visible_text('제목')
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#subContent > form > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n종로구청 " + a + "에 관한 최신공고 : ")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-1:]
            print("\n종로구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n종로구청 오류")
        webbrowser.open(url)
        print("\n", url)


def junggu(a):
    try:
        driver.implicitly_wait(15)

        url = "http://www.junggu.seoul.kr/content.do?cmsid=14232"
        driver.get(url)
        box = driver.find_element_by_name('searchValue')
        btn = driver.find_element_by_class_name("btn_search")
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > div.page > div.board_list > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n중구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:4]
            print("\n중구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                           for _ in splittext))
    except:
        print("\n중구청 오류")
        webbrowser.open(url)
        print("\n", url)


def jungnang(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.jungnang.go.kr/portal/bbs/list/B0000117.do?menuNo=200475"
        driver.get(url)
        box = driver.find_element_by_id('searchWrd')
        btn = driver.find_element_by_class_name("btn-blue")
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            '#content > div > div.table_wrap > div > table > tbody > tr:nth-child(1)')
        if not search_result:
            print("\n중랑구청 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            splittext = onlytext.split()
            del splittext[0:1]
            del splittext[-1:]
            print("\n중랑구청 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext))
    except:
        print("\n중랑구청 오류")
        webbrowser.open(url)
        print("\n", url)


def jb24(a):
    try:
        driver.implicitly_wait(15)

        url = "https://www.gov.kr/portal/locgovNews"
        driver.get(url)
        box = driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div/div/form/div[1]/div[2]/p/input')
        btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div[3]/div/div/form/div[1]/div[2]/p/span/button")
        box.send_keys(a)
        btn.click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        search_result = soup.select_one(
            'body > div.wrap > div.contentsWrap > div > div > div.unifiedSch-lst.unifiedSch3 > ul > li:nth-child(1) > dl > dt > a')
        datea = soup.select_one(
            "body > div.wrap > div.contentsWrap > div > div > div.unifiedSch-lst.unifiedSch3 > ul > li:nth-child(1) > div > span:nth-child(2)")
        if not search_result:
            print("\n정부24 에러")
            webbrowser.open(url)
        else:
            onlytext = search_result.getText()
            onlytext2 = datea.getText()
            splittext = onlytext.split()
            splittext2 = onlytext2.split()
            print("\n정부24 " + a + "에 관한 최신공고 : " + ' '.join(str(_)
                                                            for _ in splittext) + ' '.join(str(_)
                                                                                           for _ in splittext2))
    except:
        print("\n정부24 오류")
        webbrowser.open(url)
        print("\n", url)


what = input("\n검색할 문장 혹은 단어를 입력하세요 : ")

allprocess = [
      gangnam(what),
      gangdong(what),
      gangbuk(what),
      gangseo(what),
      gwangjin(what),
      guro(what),
      geumcheon(what),
      nowon(what),
      dobong(what),
      ddm(what),
      dongjak(what),
      mapo(what),
      sdm(what),
      seocho(what),
      sd(what),
      sb(what),
      songpa(what),
      yangcheon(what),
      ydp(what),
      yongsan(what),
      ep(what),
      jongno(what),
      jungnang(what),
      gwanak(what),
    jb24(what)]


for i in allprocess:
    i
    driver.delete_all_cookies()
