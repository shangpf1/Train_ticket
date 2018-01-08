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

# 列表==》 字典
stations = dict(results)

pprint(stations, indent=4)