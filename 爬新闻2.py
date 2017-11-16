# ��ȡ���ŵı��⣬���ݣ�ʱ���������
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json


def getNewsdetial(newsurl):
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    newsTitle = soup.select('.page-header h1')[0].text.strip()
    nt = datetime.strptime(soup.select('.time-source')[0].contents[0].strip(),'%Y��%m��%d��%H:%M')
    newsTime = datetime.strftime(nt,'%Y-%m-%d %H:%M')
    newsArticle = getnewsArticle(soup.select('.article p'))
    newsAuthor = newsArticle[-1]
    return newsTitle,newsTime,newsArticle,newsAuthor
def getnewsArticle(news):
    newsArticle = []
    for p in news:
         newsArticle.append(p.text.strip())
    return newsArticle

# ��ȡ��������

def getCommentCount(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
    comment = requests.get(commenturl.format(newsid))   #��Ҫ�޸ĵĵط����ɴ����ţ�����format��newsid��������ŵ�λ��
    jd = json.loads(comment.text.lstrip('var data='))
    return jd['result']['count']['total']


def getNewsLinkUrl():
#     �õ��첽��������ŵ�ַ����������з�ҳ���ŵ�ַ��
    urlFormat = 'http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&callback=newsloadercallback&_=1501000415111'
    url = []
    for i in range(1,10):
        res = requests.get(urlFormat.format(i))
        jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
        url.extend(getUrl(jd))     #entend��append������
    return url

def getUrl(jd):
#     ��ȡÿһ��ҳ�����ŵ�ַ
    url = []
    for i in jd['result']['data']:
        url.append(i['url'])
    return url

# ȡ������ʱ�䣬�༭�����ݣ����⣬����������������total_2��
def getNewsDetial():
    title_all = []
    author_all = []
    commentCount_all = []
    article_all = []
    time_all = []
    url_all = getNewsLinkUrl()
    for url in url_all:
        title_all.append(getNewsdetial(url)[0])
        time_all.append(getNewsdetial(url)[1])
        article_all.append(getNewsdetial(url)[2])
        author_all.append(getNewsdetial(url)[3])
        commentCount_all.append(getCommentCount(url))
    total_2 = {'a_title':title_all,'b_article':article_all,'c_commentCount':commentCount_all,'d_time':time_all,'e_editor':author_all}
    return total_2

# ( ������ʼ�� )��pandasģ�鴦�����ݲ�ת��Ϊexcel�ĵ�

df = pandas.DataFrame(getNewsDetial())
df.to_excel('news2.xlsx')
