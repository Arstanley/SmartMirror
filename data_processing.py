import pandas as pd
from urllib.request import urlretrieve
import re

color_num=20
std_color=pd.read_csv("./SmartMirror/lipstickData.csv")

def convert2onehot(data):
    # covert data to onehot representation
    return pd.get_dummies(data)


def convert(text):
    result = [x for x in re.split("\(|,|\)",text)if x]
    for i in range(len(result)):
        result[i]=int(float(result[i]))
    return result

def firstNumber(list):
    return list[0]
def secondNumber(list):
    return list[1]
def thirdNumber(list):
    return list[2]
def forthNumber(list):
    return list[3]
def fifthNumber(list):
    return list[4]
def sixthNumber(list):
    return list[5]

def distance(R,G,B,R1,G1,B1):
    D=(R-R1)^2+(G-G1)^2+(B-B1)^2
    return D

def ColorClassify(R,G,B):
    min = 99999
    color_class = 'A'
    for i in range(color_num):
        d = distance(R,G,B,std_color.iat[i,0],std_color.iat[i,1],std_color.iat[i,2])
        if d < min :
            min = d
            color_class = chr(ord('A') + i)
    return color_class

    # re.sub(reg_exp," ",text)
    # text_List = text.split(" ")
    # for i in range(len(text_List)) :
    #     text_List[i] = float(text_List[i])

def load_data(download=True):
    # use pandas to view the data structure
    col_names = ["FaceR","MouthR"]
    data = pd.read_csv("dataFile.csv", names=col_names)
    X = data["FaceR"].map(convert)
    Y = data["MouthR"].map(convert)
    result = X + Y
    result = pd.Series.to_frame(result)

    result['RF'] = result[0].map(firstNumber)
    result['GF'] = result[0].map(secondNumber)
    result['BF'] = result[0].map(thirdNumber)
    result['RM'] = result[0].map(forthNumber)
    result['GM'] = result[0].map(fifthNumber)
    result['BM'] = result[0].map(sixthNumber)

    result['color'] = 'A'
    for i in range(len(result)):
        result.iat[i,7] = ColorClassify(result.iat[i,4],result.iat[i,5],result.iat[i,6])


    result.drop(result.columns[[0,4,5,6]],inplace = True, axis = 1)
    print(result)
    # result.to_csv("train_data.csv")
    return result

def normalizer(data):
    r = data['RF']
    r = (r - r.mean()) / (r.std())
    data['RF'] = r

    g = data['GF']
    g = (g - g.mean()) / (g.std())
    data['GF'] = g

    b = data['BF']
    b = (b - b.mean()) / (b.std())
    data['BF'] = b
    return data





