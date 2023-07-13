fd = open("C:\\Users\\Shrinivas\\OneDrive\\Desktop\\WeatherMonitoringUsingPython\\Final\\PuneWeatherData.csv","r")
filedata = fd.readlines()
fd.close()

jsonFormat = "[\n"
for line in filedata:
    if "CityName" in line:
        continue
    datalist = line.split(",")
    citiName = datalist[0]
    state    = datalist[1]
    TempC    = datalist[2]
    TempF    = datalist[3]
    lastUpdate = datalist[4]
    localTime = datalist[5]
    localTime = localTime.strip("\n")
    
    jsonFormat +="    {\n" 
    
    jsonFormat +='     "'+"citiName"+'":"'+citiName+'"\n'
    jsonFormat +='     "'+"state"+'":"'+state+'"\n'
    jsonFormat +='     "'+"TempC"+'":"'+TempC+'"\n'
    jsonFormat +='     "'+"TempF"+'":"'+TempF+'"\n'
    jsonFormat +='     "'+"lastUpdate"+'":"'+lastUpdate+'"\n'
    jsonFormat +='     "'+"localTime"+'":"'+localTime+'"\n'
    
    jsonFormat +="    },\n" 
    
jsonFormat += "]"    
    
fd = open("C:\\Users\\Shrinivas\\OneDrive\\Desktop\\WeatherMonitoringUsingPython\\Final\\PuneWeatherDataJson.json","w")
fd.write(jsonFormat)
fd.close()
print("Json File creation done sucessfully....")