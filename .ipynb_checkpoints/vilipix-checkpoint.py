from get import *
import os

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_7246eb56b79171a6fe5284a8bf523aa0=1639057186; Hm_lpvt_7246eb56b79171a6fe5284a8bf523aa0=1639061281; Hm_lvt_0c206bb2572a8d7748c31a8a2c6c1707=1639029136,1639029216,1639061340; Hm_lpvt_0c206bb2572a8d7748c31a8a2c6c1707=1639061731',
        'DNT': '1',
        'Host': 'm.vilipix.com',
        'Pragma': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Mobile Safari/537.36 Edg/96.0.1054.43'}

pic_headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_7246eb56b79171a6fe5284a8bf523aa0=1639057311,1639108730; Hm_lpvt_7246eb56b79171a6fe5284a8bf523aa0=1639112161',
            'DNT': '1',
            'Host': 'img3.vilipix.com',
            'Pragma': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}


for i in range(1,2840+1):

    os.makedirs(f'pictures/loli/page{str(i)}',exist_ok=True)
    url = 'https://www.vilipix.com/api/illust/tag/loli?limit=30&offset='
    url += str(i)
    respone = get_html(url=url,headers=headers).json()
    print('下载json数据完成，暂停！')
    sleep(randint(3,7))
    print('暂停结束，开始分析！')
    dict1 = respone["rows"]

    for pau_list in dict1:
        pau = pau_list["regular_url"]
        file_name = pau.split('/')[-1]

        if os.path.exists(f'pictures/loli/page{str(i)}/{file_name}'):
            print(f"目录中存在{file_name}。自动跳过！")
            continue

        pic = get_html(url=pau,headers=pic_headers).content

        with open(f'pictures/loli/page{str(i)}/{file_name}',mode='wb+') as f:
            f.write(pic)
            print(f'已下载{file_name}')