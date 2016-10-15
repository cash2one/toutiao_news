import random
def get_ua(url):
    ua_list = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:43.0) Gecko/20100101 Firefox/43.0',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
               'Mozilla/4.0 (compatible; MSIE 8.0; Trident/4.0; Windows NT 6.1; SLCC2 2.5.5231; .NET CLR 2.0.50727; .NET CLR 4.1.23457; .NET CLR 4.0.23457; Media Center PC 6.0; MS-WK 8)',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
               # 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36',
               'Mozilla/4.0 (compatible; MSIE 6.00; Windows NT 5.1; SV1)',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36']
            
    host = url.split('/')[2]
    return {'Host': host,
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
            #'Cookie':'''city_name="æ­¦æ±å¸"; city_id=18''',
            'If-None-Match':'''W/"f7f88-3PhcGMQfGTJiAKTUd2Wdaw"''',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Upgrade-Insecure-Requests':'1',  
            'Referer': 'http://www.baidu.com',
            'User-Agent': ua_list[random.randint(0, 6)]
            #'User-Agent': ua_list[-1]
            }

