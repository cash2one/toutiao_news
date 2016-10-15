import sys
import time
import requests
import simplejson
from ua import get_ua
import redis
#r = redis.Redis(host="127.0.0.1",port=6379,db=0,password="")
lanmu_list = [
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&category=news_hot&as=A14507A83CD6E9B&max_behot_time=',
            'lanmu': u'热点',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_entertainment&max_behot_time=',
            'lanmu': u'娱乐',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_tech&max_behot_time=',
            'lanmu': u'科技',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_car&max_behot_time=',
            'lanmu': u'汽车',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_sports&max_behot_time=',
            'lanmu': u'体育',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_finance&max_behot_time=',
            'lanmu': u'财经',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_military&max_behot_time=',
            'lanmu': u'军事',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_fashion&max_behot_time=',
            'lanmu': u'时尚',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_world&max_behot_time=',
            'lanmu': u'国际',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_travel&max_behot_time=',
            'lanmu': u'旅游',
        },
        {
            'url': 'http://toutiao.com/api/article/recent/?source=2&count=20&as=A14507A83CD6E9B&category=news_discovery&max_behot_time=',
            'lanmu': u'探索',
        }
        # 支持扩展
    ]

def fetch_url(url,page_time):
    headers = get_ua(url)
    target_url = url + str(page_time)
    json_ = requests.get(target_url,headers=headers).content
    #print(target_url)
    json_info = simplejson.loads(json_)
    info_ = json_info['data']
    count = 0;
    for d_ in info_:
        url2 = d_['share_url']
        title = d_['title']
        print(title)
        print(url2)
        #r.sadd("item_url_s",url2)
        
    next_time = None
    try:
        next_time = json_info['next']['max_behot_time']
        print(next_time)
    except:
        pass
        return
    if next_time:
        fetch_url(url,page_time=next_time)
    return


if __name__ == '__main__':
    #第一个参数就是栏目index
    index = int(sys.argv[1])
    count = 0;
    #执行一轮翻页
    fetch_url(lanmu_list[index]['url'],page_time=0)
    #循环翻页
    '''
    while True:
        fetch_url(lanmu_list[index]['url'], lanmu_list[index]['lanmu_id'],page_time=0)
        count+=1
        print("loop",count)
    '''
