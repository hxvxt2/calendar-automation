from bs4 import BeautifulSoup
import re, os
import calendar



months = {v: k for k,v in enumerate(calendar.month_name)}
months.pop('')

all_sheets = [i for i in os.listdir('./Kill_HTML_comments.fld') if re.match('sheet...\.htm', i)]
all_sheets.sort()
soup = BeautifulSoup(open('Kill_HTML_comments.fld/sheet003.htm'), 'html.parser')

def findAllComments(soup):
    return soup.findAll('div', class_="msocomtxt")

events = []
for commentSoup in findAllComments(soup):
    anchor_selector = "_anchor_{}".format(commentSoup.get('id').strip('_com'))
    row = soup.find('span', {'id': anchor_selector}).parent.parent.parent
    date = row.findAll('td')[0].text

    author_column = None
    for td in row.findAll('td'):
        if len(td.findAll('span')) == 0:
            continue
        author_column = td

    author_name = author_column.text.strip()[:-3]
    reservation_time = commentSoup.find('font', class_="font0").text.split('\r')[0]

    events.append((date, author_name, reservation_time))
print (*events, sep = "\n")

#print ("\n".join(str(events)))