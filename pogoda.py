#/usr/bin/python3.3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

http = urlopen('http://m.pogoda.yandex.ru/?mode=short')
soup = BeautifulSoup(http)
print('\n', soup.title.string)
my = soup.findAll(name='div', attrs={'class': 'b-details'})

f = open('weather.txt', 'w')
for m in my:
    res = m.findAll(text=True)
    rep = ' '.join(str(e) for e in res)
    f.write('\n%s\n' % rep)
f.close()


def replace_line_file(source_text, replace_text):
    file = open('weather.txt')
    text = file.read()
    file.close()
    file = open('weather.txt', 'w')
    file.write(text.replace(source_text, replace_text))
    file.close()

replace_line_file('утро', '\nутро:')
replace_line_file('день', '\nдень:')
replace_line_file('вечер', '\nвечер:')
replace_line_file('ночь', '\nночь:')

for n,line in enumerate(open('weather.txt')):
    if n in [0,1,2,3,4,5]:
        print(line.rstrip())
    if n in [6,7,8,9,10,11,12]:
        print(line.rstrip())

