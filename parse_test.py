
import requests 
import re
from pprint import pprint

url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955"

r = requests.get(url)

# 正则表达式==> 解析
"""
results 正则匹配
"""
stations = r.text
results = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', stations)

'''
思路： city = ['北京','上海']
       code = ['BJ','SH'] 

'''
results = dict(results)


print(results.keys())
print(results.values())