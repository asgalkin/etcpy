#!/usr/bin/env python3.3
# -*- coding: utf-8 -*-

from requests import session
from bs4 import BeautifulSoup


def stat(service, login, password):
    """ Состояние счёта """
    payload = {'LoginForm[login]': login, 'LoginForm[password]': password}
    with session() as c:
        c.post('https://lk.vologda.mts.ru/index.php?r=site/login', data=payload, verify=False)
        request = c.get('https://lk.vologda.mts.ru/index.php?r=account/index')
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text)
    tags = soup.find_all(name='h4', attrs={'class': 'relative'})
    for txt in tags:
        text = txt.findAll(text=True)
        rep = ''.join(text).split()
        print(service, rep[2], '\nБаланс:', rep[5], 'руб')

stat('Интернет', 'YOUR_LOGIN', 'YOUR_PASSWORD')
print()
stat('Телевидение', 'YOUR_LOGIN', 'YOUR_PASSWORD')