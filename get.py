import requests
import parsel
from random import randint
from time import sleep

def get_html(url:str,headers={},time=5,sleepmode=True,sb=3,sm=7):
    while time > 0:
        try:
            print(f"正在发送请求。链接为"+url)
            if headers == {}:
                respone = requests.get(url=url)
            else:
                respone = requests.get(url=url,headers=headers)
            if sleepmode:
                sleeptime = randint(sb,sm)
                print(f'睡眠开始！共计睡眠{sleeptime}秒！')
                sleep(sleeptime)
        except requests.exceptions.ConnectionError as e:
            print(f"无法连接到服务器！错误为：{e}正在重试！")
            print(f'还剩下{time}次重试机会！')
            time -= 1
            continue
        else:
            print('请求发送成功！')
            break
    else:
        print('错误次数过大！跳过！')
        return "None"
    return respone

def get_data(respone_text:str,xpath:str):
    selector1 = parsel.Selector(respone_text)
    list1 = selector1.xpath(xpath)
    return list1