import requests
from bs4 import BeautifulSoup
import re

print("What difficulty do you need : ",end="")

difficulty = input()

load_url = "https://atcoder.jp/contests/typical90/tasks"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

target_url = []
for i in soup.find_all("a"):
    if "★"+difficulty in str(i):
        target_url.append(i)


test_a = ''' <a href="/contests/typical90/tasks/typical90_m">Passing（★5）</a>'''

#urlと問題名を正規表現を使って取得
pattern_url = r'\"(.*)\"' 
pattern_name = r'\>(.*)\<'

url_name_pair = []
for e,i in enumerate(target_url):
    url_name_pair.append([re.findall(pattern_url, str(i)),re.findall(pattern_name, str(i))])   
    
    
#相対urlなので前半の部分を付け足す
original_url = "https://atcoder.jp"
target_url2 = []
for e,i in enumerate(url_name_pair):
    target_url2.append([original_url + i[0][0],i[1][0]])

print("# ☆"+difficulty)
for i in target_url2:
    print("## "+i[1])
    print("- [ ]  ["+i[0]+"]"+"("+i[0]+")")