fd = open("G:\\WeatherMonitorig\\_out\\PuneWeatherData.csv","r")
filedata = fd.readlines()
fd.close()
 
xmlFormat = "<TempratureData>\n\n"

for line in filedata:
    datalist = line.split(",")
    citiName = datalist[0]
    state    = datalist[1]
    TempC    = datalist[2]
    TempF    = datalist[3]
    lastUpdate = datalist[4]
    localTime = datalist[5]
    localTime = localTime.strip("\n")
    
    xmlFormat += "    <City>"+citiName+"</City>\n"
    xmlFormat += "    <State>"+state+"</State>\n"
    xmlFormat += "    <TempC>"+TempC+"</TempC>\n"
    xmlFormat += "    <TempF>"+TempF+"</TempF>\n"
    xmlFormat += "    <lastUpdate>"+lastUpdate+"</lastUpdate>\n"
    xmlFormat += "    <localTime>"+localTime+"</localTime>\n"
    xmlFormat += "\n"
    
xmlFormat += "</TempratureData>\n"

fd = open("G:\\WeatherMonitorig\\_out\\PuneWeatherDataXml.xml","w")
fd.write(xmlFormat)
fd.close()
print("XML File creation done sucessfully...")