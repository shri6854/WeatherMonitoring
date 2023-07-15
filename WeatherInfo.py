import requests
import sys
import json
import os
import argparse
 
# Global Variales
Name = ""
State = ""
LocalTime = ""
Temp_C = ""
Temp_F = ""
LastUpadted = ""
query = "" 
outpath = ""

##################################################################
# Function Name :  ExtractData
# Arguments     :  query
# Return Value  :  None
# Called By     :  None
# Description   :  Extract data using api
##################################################################
def ExtractData(query):
    # Try to extract data using API
    try:
        print(query)
        apiResponce = requests.get(query)
    except:
        sys.exit("Error: Data Extraction Not Possible.")
        
    return apiResponce
    
##################################################################
# Function Name :  ExtractFields
# Arguments     :  responce
# Return Value  :  None
# Called By     :  None
# Description   :  Collect required data from responce
##################################################################
def ExtractFields(responce):
    print(responce)
    global Name, State, LocalTime, Temp_C, Temp_F, LastUpadted
    Name = responce.json()["location"]["name"]
    State = responce.json()["location"]["region"]
    LocalTime = responce.json()["location"]["localtime"]
    Temp_C = responce.json()["current"]["temp_c"]
    Temp_F = responce.json()["current"]["temp_f"]
    LastUpadted = responce.json()["current"]["last_updated"]

##################################################################
# Function Name :  processData
# Arguments     :  None
# Return Value  :  None
# Called By     :  None
# Description   :  Process Api Data
##################################################################
def processData():
    # Convert datatype from float to string 
    Temp_C1 = str(Temp_C)
    Temp_F1 = str(Temp_F)
    
    # Epmty List
    dataList = []
    
    # Append fields to list
    dataList.append(Name)
    dataList.append(State)
    dataList.append(Temp_C1)
    dataList.append(Temp_F1)
    dataList.append(LastUpadted)
    dataList.append(LocalTime)
    ForPrint = ",".join(dataList)
    ForPrint = ForPrint+"\n"
    return ForPrint
    
    # Anather way using string concatination
# ForPrint = Name +","+ State +","+ Temp_C +","+Temp_F +","+LastUpadted +","+ LocalTime+"\n"

##################################################################
# Function Name :  printFile
# Arguments     :  forWrite, outpath
# Return Value  :  None
# Called By     :  None
# Description   :  Write Data in file
##################################################################
def printFile(forWrite,outpath):
    # Create absolute file path
    path = outpath + Name +"WeatherData.csv"
    if(os.path.exists(path) == False):
        fd = open(path,"w")
        fd.write("CityName,State,TemperatureCelsius,TemperatureFah,LastUpdate,LocalTime\n")
        fd.write(forWrite)
        fd.close()
        print("File Creation Done...\nData Write successfully...")
    else:
        fd = open(path,"a")
        fd.write(forWrite)
        fd.close()
        print("Data append successfully...")
        
##################################################################
# Function Name :  acceptInput
# Arguments     :  None
# Return Value  :  None
# Called By     :  None
# Description   :  Take input arguments from user
##################################################################
def acceptInput():
    global query, outpath
    parser = argparse.ArgumentParser(description = "Script to show weather data")
    
    parser.add_argument("-query","--query", type=str, nargs=1, default=None, required=True)
    parser.add_argument("-outpath","--outpath", type=str, nargs=1, default=None, required=True)
    
    # Parse input arguments and collect it in variable
    args = parser.parse_args()
    query = args.query[0]
    outpath = args.outpath[0]
    
##################################################################
# Function Name :  main
# Arguments     :  None
# Return Value  :  None
# Called By     :  None
# Description   :  main function
##################################################################
def main():
    acceptInput()
    responce = ExtractData(query)
    ExtractFields(responce)
    forWrite = processData()
    printFile(forWrite,outpath)
    
if __name__== '__main__':
    main()
    

