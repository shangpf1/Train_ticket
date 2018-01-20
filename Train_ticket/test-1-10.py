'''
"车次 出发站 到达站 出发时间 到达时间 历时 商务座 特等座 一等座 二等座 高级 软卧 动卧 硬卧 软座 硬座 无座"
['G1234','AOH','LAJ','06:09','12;30','06:21','120','无','无','','',','','','','']

'''

info = "车次 出发站 到达站 出发时间 到达时间 历时 商务座 特等座 一等座 二等座 高级 软卧 动卧 硬卧 软座 硬座 无座" 

info = info.split(" ")

traininfo = "XKHbBE5qfNEm1yT%2BhQcvnZq6Jm%2FAo0bli%2FU8Et1N45yZtrZ6LVYUQsgU41aQgPxv4faF1d6EV2VO%0A4Eb1Ay8fjOge0Dl5xLS8tMzUKbM23hIKLG%2BC9Oyi6JzO0%2BExKMi0h7iROk18IWEgsZuQdtGPiDDR%0AssbWWkMuq%2Fd2AJYlm7hdUqlSRJK94rOb9i5r5DuuFPBsAHIOhb2qeAkT4Tex6BtZTY6oR0fcwBSU%0Ae2K8wX8zrAOnm3LMSnN62d15tMQPRvdmoA%3D%3D|预订|240000G1010D|G101|VNP|AOH|VNP|AOH|06:43|12:39|05:56|Y|qCLmi0H4RaZnKStT22x5xlcWVNUPqtpf01K24Hi6NQFCCjkD|20180113|3|P2|01|11|1|0|||||||||||有|有|有||O0M090|OM9|0"

trainlist = traininfo.split("|")
# print(trainlist)
# for index,value in enumerate(trainlist):
#     print(index,"===>",value)

trainrow = []
trainrow.extend(trainlist[3:6])
trainrow.extend(trainlist[8:11])
trainrow.extend(trainlist[21:32])

print(info)

print(trainrow)

from prettytable import PrettyTable

# x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
x = PrettyTable(info)
x.add_row(trainrow)

# x = PrettyTable(['车次', '出发站', '到达站', '出发时间', '到达时间', '历时', '商务座', '特等座', '一等座', '二等座', '高级', '软卧', '动卧', '硬卧', '软座', '硬座', '无座'])
# X.add_row(['G101', 'VNP', 'AOH', '06:43', '12:39', '05:56', '', '', '', '', '', '', '', '', '', '', '有', '有'])

# x.set_field_names(["City name", "Area", "Population", "Annual Rainfall"])
# x.add_row(["Adelaide",1295, 1158259, 600.5])
# x.add_row(["Brisbane",5905, 1857594, 1146.4])
# x.add_row(["Darwin", 112, 120900, 1714.7])
# x.add_row(["Hobart", 1357, 205556, 619.5])
# x.add_row(["Sydney", 2058, 4336374, 1214.8])
# x.add_row(["Melbourne", 1566, 3806092, 646.9])
# x.add_row(["Perth", 5386, 1554769, 869.4])

print(x.get_string())

