# -*- encoding: utf-8 -*-
# date: 2019年8月1日17:23:33

import csv
import os
import datetime


fileName="weightData.csv"
filepath = os.getcwd() + os.sep + "dota" + os.sep   # 在当前进程根目录下创建 dota 文件夹
if not os.path.exists(filepath+fileName):
    os.makedirs(filepath)
    # 创建文件
    with open(filepath+fileName, "w+", encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        head = ["index", "datetime", "Dispenser","pulsTime(ms)","cycleTime(ms)","dotNum","totalWeight","potWeight"]
        writer.writerow(head)

# print(os.getcwd())
# 读
with open(fileName, "r+") as csvfile:
    lines = csvfile.readlines()
    lastLine = lines[-1].split(',')
if lastLine[0] == "index":
    index = 0
else:
    index = int(lastLine[0])

# 追加 'a+' 添加到文件后
with open(fileName, "a+", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    datas = [index + 1, datetime.datetime.now(),'a1', 'b1']
    writer.writerow(datas)

with open(fileName, "r+") as csvfile:
    readr = csv.reader(csvfile)
    for line in readr:
        print(line)