import colorgram
import pandas as pd
import json
from collections import OrderedDict

rgb_data = []

def loadCSV():
  global rgb_data
  rgb_data = pd.read_csv('rgb.csv', sep=',',header=None)

def convertFromRgbToWebColour(imageRGB):

  loadCSV()
  
  nearest = ''
  diff = ''
  target = imageRGB

  for index, row in rgb_data.iterrows():

    red = abs(row[1] - target[0])
    green = abs(row[2] - target[1])
    blue = abs(row[3] - target[2])

    total = red + green + blue

    if not diff:
      nearest = row[0]
      diff = total
    else:
      if total < diff:
        nearest = row[0]
        diff = total

  return nearest


def getImageRGB(imagePath,numberColours):

  results = []

  colors = colorgram.extract(imagePath, numberColours)

  for x in colors:
    rgb = x.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    
    imageVales = [red,green,blue]
    imageColor = convertFromRgbToWebColour(imageVales)
    results.append(imageColor)

  return json.dumps(list(OrderedDict.fromkeys(results)))

print getImageRGB('t.jpg',6)