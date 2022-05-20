import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
#from bitmap import BitMapImage
#from bitmap import Image as BitMapImage
#import bitmaptest
import bitmaputils
import math

from IPython.display import Image as IPImage
from PIL import Image as PILImage

KelvinTable = {
    1000: [255, 56, 0],
    1100: [255, 71, 0],
    1200: [255, 83, 0],
    1300: [255, 93, 0],
    1400: [255, 101, 0],
    1500: [255, 109, 0],
    1600: [255, 115, 0],
    1700: [255, 121, 0],
    1800: [255, 126, 0],
    1900: [255, 131, 0],
    2000: [255, 138, 18],
    2100: [255, 142, 33],
    2200: [255, 147, 44],
    2300: [255, 152, 54],
    2400: [255, 157, 63],
    2500: [255, 161, 72],
    2600: [255, 165, 79],
    2700: [255, 169, 87],
    2800: [255, 173, 94],
    2900: [255, 177, 101],
    3000: [255, 180, 107],
    3100: [255, 184, 114],
    3200: [255, 187, 120],
    3300: [255, 190, 126],
    3400: [255, 193, 132],
    3500: [255, 196, 137],
    3600: [255, 199, 143],
    3700: [255, 201, 148],
    3800: [255, 204, 153],
    3900: [255, 206, 159],
    4000: [255, 209, 163],
    4100: [255, 211, 168],
    4200: [255, 213, 173],
    4300: [255, 215, 177],
    4400: [255, 217, 182],
    4500: [255, 219, 186],
    4600: [255, 221, 190],
    4700: [255, 223, 194],
    4800: [255, 225, 198],
    4900: [255, 227, 202],
    5000: [255, 228, 206],
    5100: [255, 230, 210],
    5200: [255, 232, 213],
    5300: [255, 233, 217],
    5400: [255, 235, 220],
    5500: [255, 236, 224],
    5600: [255, 238, 227],
    5700: [255, 239, 230],
    5800: [255, 240, 233],
    5900: [255, 242, 236],
    6000: [255, 243, 239],
    6100: [255, 244, 242],
    6200: [255, 245, 245],
    6300: [255, 246, 247],
    6400: [255, 248, 251],
    6500: [255, 249, 253],
    6600: [254, 249, 255],
    6700: [252, 247, 255],
    6800: [249, 246, 255],
    6900: [247, 245, 255],
    7000: [245, 243, 255],
    7100: [243, 242, 255],
    7200: [240, 241, 255],
    7300: [239, 240, 255],
    7400: [237, 239, 255],
    7500: [235, 238, 255],
    7600: [233, 237, 255],
    7700: [231, 236, 255],
    7800: [230, 235, 255],
    7900: [228, 234, 255],
    8000: [227, 233, 255],
    8100: [225, 232, 255],
    8200: [224, 231, 255],
    8300: [222, 230, 255],
    8400: [221, 230, 255],
    8500: [220, 229, 255],
    8600: [218, 229, 255],
    8700: [217, 227, 255],
    8800: [216, 227, 255],
    8900: [215, 226, 255],
    9000: [214, 225, 255],
    9100: [212, 225, 255],
    9200: [211, 224, 255],
    9300: [210, 223, 255],
    9400: [209, 223, 255],
    9500: [208, 222, 255],
    9600: [207, 221, 255],
    9700: [207, 221, 255],
    9800: [206, 220, 255],
    9900: [205, 220, 255],
    10000: [207, 218, 255],
    10100: [207, 218, 255],
    10200: [206, 217, 255],
    10300: [205, 217, 255],
    10400: [204, 216, 255],
    10500: [204, 216, 255],
    10600: [203, 215, 255],
    10700: [202, 215, 255],
    10800: [202, 214, 255],
    10900: [201, 214, 255],
    11000: [200, 213, 255],
    11100: [200, 213, 255],
    11200: [199, 212, 255],
    11300: [198, 212, 255],
    11400: [198, 212, 255],
    11500: [197, 211, 255],
    11600: [197, 211, 255],
    11700: [197, 210, 255],
    11800: [196, 210, 255],
    11900: [195, 210, 255],
    12000: [195, 209, 255]};


def getTempFromColourNew(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    #emp = int((r*256*256 + g*256 + b)/10000)
    temp = (r*256*256 + g*256 + b)/100000
    return temp

def getColourFromTempNew(temp, i, j):
    temp1 = int(temp * 100000)
    b = int(temp1 % 256)
    temp2 = int(temp1/256)
    g = int(temp2 % 256)
    r = int(temp2/256)
    #return [r, g, b];
    pixel = list()
    pixel.append(r)
    pixel.append(g)
    pixel.append(b)
    #if ((i==99)and(j==99)):
    #   print("getColourFromTempNew : i=", i, " j=", j, " temp=", temp, " pixel00=", pixel)
    return pixel;

def computerHeatMap(tempArray, targetTemp, curTime):
    pdata1 = [[[0]*3 for i in range(width)] for row in range(height)]
    MinTemp2 = 99999;
    MaxTemp2 = 0;
    pdata00=[]
    for i in range(height):
        for j in range(width):
            #temp = tempArray[i][j] - (tempReductionPerMin * minutes);
            temp = tempArray[i][j] + (targetTemp-tempArray[i][j])*curTime/targetTime;
            pdata1[i][j] = getColourFromTempNew(temp, i, j)
            temp2 = getTempFromColourNew(pdata1[i][j])
            if temp2 < MinTemp2:
                MinTemp2 = int(temp2)
            if temp2 > MaxTemp2:
                MaxTemp2 = int(temp2)

    print(f"Temperature after {curTime} minutes: min={MinTemp2} max={MaxTemp2}")
    # Make Numpy array from list
    na1 = np.array(pdata1, dtype=np.uint8)
    #na1 = np.flip(na1, 0)
    plt.figure()
    resultimg = plt.imshow(na1, interpolation='none')

def showTemperatureVariation(tempArray, targetTemp, targetTime):
    minTemp = [99999]*targetTime
    maxTemp = [0]*targetTime
    Temps = range(targetTime)
    for curt in range(targetTime):
        for i in range(height):
            for j in range(width):
                temp = tempArray[i][j] + (targetTemp-tempArray[i][j])*curt/targetTime;
                if temp < minTemp[curt]:
                    minTemp[curt] = int(temp)
                if temp > maxTemp[curt]:
                    maxTemp[curt] = int(temp)
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(Temps, minTemp, label="Min temperature")
    ax.plot(Temps, maxTemp, label="Max temperature")
    plt.title("Variation of minimum and maximum temperature over time")
    plt.xlabel("Time")
    plt.ylabel("Temperature")
    #plt.xticks(np.arange(0, targetTime+1, step=2), np.arange(0, targetTime+1, step=2))
    #plt.yticks(np.arange(0, 210, step=10))
    plt.legend()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    plt.show()
    
imageName = r'Documents\18401_87a_Avenue_NW-24.bmp'

# Display initial heat-map
bmpo = PILImage.open(imageName)
#plt.figure()
#plt.imshow(bmpo,vmin=0,vmax=255)

with open(imageName, "rb") as file:
    #a = Image(file.read())
    fh = file.read()
    #img = BitMapImage(fh)
    #img = bitmaptest.Image(fh)
    img = bitmaputils.Image(fh)

width = img.getBitmapWidth()
height = img.getBitmapHeight()
pdata0 = img.getPixels()
print(f"Image width={width} height={height}")

# Make Numpy array from list
na0 = np.array(pdata0, dtype=np.uint8)
plt.figure()
resultimg = plt.imshow(na0, interpolation='none')


# Compute temperature from heatmap
#tempArray = []
tempArray = np.zeros((height, width))

MinTemp1 = 99999;
MaxTemp1 = 0;
for i in range(height):
    for j in range(width):
        tempArray[i][j] = getTempFromColourNew(pdata0[i][j])
        if tempArray[i][j] < MinTemp1:
            MinTemp1 = int(tempArray[i][j])
        if tempArray[i][j] > MaxTemp1:
            MaxTemp1 = int(tempArray[i][j])

print(f"Inital temperature: min={MinTemp1} max={MaxTemp1}")

# Process using Internet of Things

# Inject cold airflow for 10 minutes
#for i in range(height):
#    for j in range(width):
#        tempArray[i][j] = tempArray[i][j] - (tempReductionPerMin * minutes);

#
#tempReductionPerMin = 10
targetTemp = 25
targetTime = 30
print(f"Target: temperature={targetTemp} duration={targetTime}")
#
# Inject cold airflow for 10 minutes
computerHeatMap(tempArray, targetTemp, 10)
# Inject cold airflow for 20 minutes
computerHeatMap(tempArray, targetTemp, 20)
# Inject cold airflow for 30 minutes
computerHeatMap(tempArray, targetTemp, 30)
showTemperatureVariation(tempArray, targetTemp, targetTime)

targetTemp = 15
targetTime = 30
print(f"Target: temperature={targetTemp} duration={targetTime}")
#
# Inject cold airflow for 10 minutes
computerHeatMap(tempArray, targetTemp, 10)
# Inject cold airflow for 20 minutes
computerHeatMap(tempArray, targetTemp, 20)
# Inject cold airflow for 30 minutes
computerHeatMap(tempArray, targetTemp, 30)
showTemperatureVariation(tempArray, targetTemp, targetTime)

# Display
#img2.save('result.png')
#plt.imshow(img2,vmin=0,vmax=255)
#img2.show()

# Display final heat-map

