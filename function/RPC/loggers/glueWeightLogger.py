# -*- encoding: utf-8 -*-

import datetime
import os
import csv
import sys

def  glueWeightLogger(weightDatalist=[],fileName="weightData.csv"):
    """
     "Dispenser","pulsTime(ms)","cycleTime(ms)","dotNum","totalWeight","potWeight",
                    "DotUpperWeight_D","DotLowerWeight_D","ptDotRefWeight_D"

    :param strdata: "Dispenser","pulsTime(ms)","cycleTime(ms)","dotNum","totalWeight","potWeight",
                    "DotUpperWeight_D","DotLowerWeight_D","ptDotRefWeight_D"
    :param fileName:
    :return:
    """

    if sys.platform == "darwin":
        filePath = os.getcwd() + os.sep +"/vault/weightData/"
    elif sys.platform == "win32":
        filePath = os.getcwd() + os.sep + "vault\\weightData\\"

    if not os.path.exists(filePath):
        os.makedirs(filePath)
        # 创建文件
        with open(filePath+fileName, "w+", encoding='utf8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            head = ["index", "datetime", "Dispenser","pulsTime(ms)","cycleTime(ms)","dotNum","totalWeight(mg)","potWeight(mg)",
                    "DotUpperWeight(mg)","DotLowerWeight(mg)","ptDotRefWeight(mg)"]
            writer.writerow(head)

    # print(os.getcwd())
    # 读
    with open(filePath+fileName, "r+") as csvfile:
        lines = csvfile.readlines()
        lastLine = lines[-1].split(',')
    if lastLine[0] == "index":
        index = 0
    else:
        index = int(lastLine[0])

    # 追加 'a+' 添加到文件后
    with open(filePath+fileName, "a+", encoding='utf8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        datas = [index + 1,datetime.datetime.now()] + weightDatalist
        writer.writerow(datas)

    # with open(filePath+fileName, "r+") as csvfile:
    #     readr = csv.reader(csvfile)
    #     for line in readr:
    #         print(line)


#
if __name__ == '__main__':
    glueWeightLogger()

    