#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 23:49:37 2018

@author: apple
"""

# -*- coding: UTF-8 -*-  
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Baidu AIP SDK
"""
# -*- coding:utf-8 -*-

from aip import AipFace
import json
import base64
from PIL import Image
import os 
import pandas as pd 
from pandas import Series, DataFrame

# 定义常量
APP_ID = '11565043'
API_KEY = '8iKksmE52bSq9fNev6jqV12v'
SECRET_KEY = 'BzVIMw5CIrZKnMgHiurMRQlWiUS0AvFE'

# 设置人脸识别参数（全局）
options = {}
options["face_field"] = "landmark"
options["max_face_num"] = 1
nameList = []
kouhongrgb = []
skinColorRgb = []
###Function to create a list for the filenames in the directory
def getAverage(x, y):
	return (x+y)/2

def listDir(rootDir):
	for filename in os.listdir(rootDir):
		pathname = os.path.join(rootDir, filename)
		if (os.path.isfile(filename)):
			nameList.append(pathname)

def getAverageRGB(sampleLandmark72):
	x1 = landmark72[59]['x'] 

# 初始化AipFace对象  
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
listDir('/Users/Arstan/Documents/Hackathon')

for i in nameList[2000:2500]:
	with open(i, "rb") as f:
		base64_data = base64.b64encode(f.read())
	
	print(str(nameList.index(i)) + '/' + str(len(nameList)))

	result = aipFace.detect(str(base64_data)[2:], "BASE64", options)
	if result['error_code'] == 0:

		landmark72 = result['result']['face_list'][0]['landmark72']
		

		# 计算口红颜色（取嘴唇上的六个点然后取rgb平均值
		im = Image.open(i)
		pix = im.load()

		x_1, y_1 = landmark72[59]['x'], landmark72[59]['y']
		x_2, y_2 = landmark72[66]['x'], landmark72[66]['y']
		x1 = getAverage(x_1, x_2)
		y1 = getAverage(y_1, y_2)

		r1, g1, b1 = pix[x1,y1]

		x_1, y_1 = landmark72[60]['x'], landmark72[60]['y']
		x_2, y_2 = landmark72[67]['x'], landmark72[67]['y']
		x2 = getAverage(x_1, x_2)
		y2 = getAverage(y_1, y_2)

		r2, g2, b2 = pix[x2,y2]

		x_1, y_1 = landmark72[61]['x'], landmark72[61]['y']
		x_2, y_2 = landmark72[68]['x'], landmark72[68]['y']
		x3 = getAverage(x_1, x_2)
		y3 = getAverage(y_1, y_2)

		r3, g3, b3 = pix[x3,y3]

		x_1, y_1 = landmark72[71]['x'], landmark72[71]['y']
		x_2, y_2 = landmark72[65]['x'], landmark72[65]['y']
		x4 = getAverage(x_1, x_2)
		y4 = getAverage(y_1, y_2)

		r4, g4, b4 = pix[x4,y4]

		x_1, y_1 = landmark72[70]['x'], landmark72[70]['y']
		x_2, y_2 = landmark72[64]['x'], landmark72[64]['y']
		x5 = getAverage(x_1, x_2)
		y5 = getAverage(y_1, y_2)

		r5, g5, b5 = pix[x5,y5]


		x_1, y_1 = landmark72[69]['x'], landmark72[69]['y']
		x_2, y_2 = landmark72[63]['x'], landmark72[63]['y']
		x6 = getAverage(x_1, x_2)
		y6 = getAverage(y_1, y_2)

		r6, g6, b6 = pix[x6,y6]

		r = int((r1+r2+r3+r4+r5+r6)/6)
		g = int((g1+g2+g3+g4+g5+g6)/6)
		b = int((b1+b2+b3+b4+b5+b6)/6)

		rgb = (r,g,b)
		kouhongrgb.append(rgb)

	    # 提取肤色rgb

		x_1, y_1 = landmark72[48]['x'], landmark72[48]['y']
		x_2, y_2 = landmark72[55]['x'], landmark72[55]['y']
		x1 = getAverage(x_1, x_2)
		y1 = getAverage(y_1, y_2)

		r1, g1, b1 = pix[x1,y1]

		x_1, y_1 = landmark72[1]['x'], landmark72[1]['y']
		x_2, y_2 = landmark72[49]['x'], landmark72[49]['y']
		x2 = getAverage(x_1, x_2)
		y2 = getAverage(y_1, y_2)

		r2, g2, b2 = pix[x2,y2]

		x_1, y_1 = landmark72[54]['x'], landmark72[54]['y']
		x_2, y_2 = landmark72[11]['x'], landmark72[11]['y']
		x3 = getAverage(x_1, x_2)
		y3 = getAverage(y_1, y_2)

		r3, g3, b3 = pix[x3,y3]
	    
		r = int((r1+r2+r3)/3)
		g = int((g1+g2+g3)/3)
		b = int((b1+b2+b3)/3)

		rgb = (r,g,b)
		skinColorRgb.append(rgb)
 

s = Series( kouhongrgb, index = skinColorRgb)

s.to_csv("dataFile5.csv")




# 解析位置信息





# plt.show()