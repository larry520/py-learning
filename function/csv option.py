# -*- encoding: utf-8 -*-
# date: 2019年8月1日17:23:33

import csv

# 写
with open("test.csv", "w", encoding='utf8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["index", "a_name", "b_name"])
    writer.writerows([[0, 'a1', 'b1'], [1, 'a2', 'b2'], [2, 'a3', 'b3']])

# 读
with open("test.csv", "r") as csvfile:
    readr = csv.reader(csvfile)
    for line in readr:
        print(line)

import datetime

print(datetime.datetime.now())
