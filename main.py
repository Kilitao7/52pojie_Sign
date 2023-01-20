# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

def sign(cookie):
    result = ""
    headers = {
        "Cookie": cookie,
        "ContentType": "text/html;charset=gbk",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=headers
    )
    fa = requests.session().put(
        "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers
    )
    fb = BeautifulSoup(fa.text, "html.parser")
    fc = fb.find("div", id="messagetext").find("p").text
    if "您需要先登录才能继续本操作" in fc:
        result += "Cookie 失效"
    elif "恭喜" in fc:
        requests.get("https://sctapi.ftqq.com/SCT175451TwBA4biGKp0QSKAMR2YtH3O5x.send?title=吾爱破解签到成功！")
        result += "签到成功"
    elif "不是进行中的任务" in fc:
        result += "今日已签到"
    else:
        result += "签到失败"
    return result 

def main():
    b = os.environ['POJIE']
    cookie = b
    cookie = "wzws_sessionid=oGPKMLOAMzYuMTQyLjEzNS4xMzCBYjM2YmFhgmRiMWNhYQ==; htVC_2132_saltkey=a1Qz93m3; htVC_2132_lastvisit=1674191507; htVC_2132_seccodecSwQE=6751129.76c3a2cab861bd0991; htVC_2132_ulastactivity=1674195128%7C0; htVC_2132_auth=32fc9rt%2B%2BHcRRgnEMm6du4yyp8pODHs4iqOuUHwkZ9T0Ok41Galcu3Q7a653Ph2DDzmLmxV3ylcIyIs9gnsF8qz2%2Fn0b; htVC_2132_lip=36.142.135.130%2C1674195128; htVC_2132_connect_is_bind=1; htVC_2132_seccodecS=6751151.59b1d7442c1765f01a; htVC_2132_sid=0; htVC_2132_nofavfid=1; htVC_2132_noticonf=1148795D1D3_3_1; htVC_2132_ttask=1148795%7C20230120; wzws_sid=2458fee8016af69dc60a58f2af20370b279a8bb2f1888ea85f42c39a2d5ee7a9570583319d2814db0f9522a42e3435aa7e9b108513a2215d7fc67fda525e8b14768767d29fb89c16b416c1b7ad084e26b473795d500055c04d6508fe28843733; htVC_2132_checkpm=1; htVC_2132_lastcheckfeed=1148795%7C1674196302; htVC_2132_checkfollow=1; htVC_2132_lastact=1674196311%09home.php%09task"
    sign_msg = sign(cookie=cookie)
    print(sign_msg)


if __name__ == "__main__":
    main()
