import requests
 
fd1 = open("G:\\WeatherMonitorig\\_out\\PuneWeatherData.csv","r")
filedata1 = fd1.readlines()
fd1.close()

fd2 = open("G:\\WeatherMonitorig\\_out\\BengaluruWeatherData.csv","r")
filedata2 = fd2.readlines()
fd2.close()

fd3 = open("G:\\WeatherMonitorig\\_out\\HyderabadWeatherData.csv","r")
filedata3 = fd3.readlines()
fd3.close()

# fd4 = open("G:\\WeatherMonitorig\\_out\\PuneWeatherData.csv","r")
# filedata4 = fd4.readlines()
# fd4.close()

mydata1 = filedata1[-1].split(",")
TempData1 = '\nCity: {}\nState: {}\nTemp in celsius: {}\nTemp in fahrenheit: {}\nLast Upadated: {}\n'.format(mydata1[0], mydata1[1],mydata1[2],mydata1[3],mydata1[4])

mydata2 = filedata2[-1].split(",")
TempData2 = '\nCity: {}\nState: {}\nTemp in celsius: {}\nTemp in fahrenheit: {}\nLast Upadated: {}\n'.format(mydata2[0], mydata2[1],mydata2[2],mydata2[3],mydata2[4])

mydata3 = filedata3[-1].split(",")
TempData3 = '\nCity: {}\nState: {}\nTemp in celsius: {}\nTemp in fahrenheit: {}\nLast Upadated: {}\n'.format(mydata3[0], mydata3[1],mydata3[2],mydata3[3],mydata3[4])

# mydata4 = filedata4[-1].split(",")
# TempData4 = '\nCity: {}\nState: {}\nTemp in celsius: {}\nTemp in fahrenheit: {}\nLast Upadated: {}\n'.format(mydata4[0], mydata4[1],mydata4[2],mydata4[3],mydata4[4])

header = "Weather data for {} \n".format(mydata1[4])

TempData = header + TempData1 + TempData2 + TempData3

url = "https://api.telegram.org/bot2079377568:AAHy8ZMyeBVW-V5wigdc55rHVRltDPmMX14/sendMessage?chat_id=-1001619895423&text="
text = '"'+ TempData + '"'
api =  url + text
try:
    response = requests.post(api)
except:
    print("\nError : Data sending on telegram channel failed...\n")
    exit(-1)

if str(response) == "<Response [200]>":
    print("\nData Sent on telegram channel succesffuly...")

    
