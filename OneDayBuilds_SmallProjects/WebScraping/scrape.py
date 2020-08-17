from bs4 import BeautifulSoup
import requests
import csv

#example on how to scrape a website
#with open('basicHtml.html') as html_file:
#    soup = BeautifulSoup(html_file,'lxml')

#print(soup.prettify())
#match = soup.title.text
#match = soup.find('div',class_='Footer')
#print(match)

#article = soup.find('div',class_='Article')
#print(article)
#headline = article.h2.a.text
#print(headline)
#summary = article.p.text
#print(summary)

#articles = soup.find_all('div',class_='Article')

#for article in articles:
#    headline = article.h2.a.text
#    print(headline)
#    summary = article.p.text
#    print(summary)
#    print()

#actual project
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

csv_file = open('cms_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

for article in soup.find_all('article'):
    #print(article.prettify())
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div',class_ = 'entry-content').p.text
    print(summary)

    try:
        vid_src = article.find('iframe',class_='youtube-player')['src']
        vid_id = vid_src.split('/')[4]
        vid_id = vid_id.split('?')[0]

        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()
