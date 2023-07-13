from WeatherInfo import ExtractData

myapi = "http://api.weatherapi.com/v1/current.json?key=015b3c52dcfe424ca5a193028211710&q=Pune&aqi=yes"

result = ExtractData(myapi)
myresp = str(result)

if myresp == "<Response [200]>":
    print("Passed")
else:
    print("Not passed")