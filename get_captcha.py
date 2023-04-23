# -*- coding: utf-8 -*-
"""
1.获取验证码
"""
import requests
import uuid

for i in range(1, 200):
    resp = requests.get('http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml')
    with open('source/' + str(uuid.uuid4()) + '.png', 'wb') as f:
        f.write(resp.content)