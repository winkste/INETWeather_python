from time import localtime,  sleep 
import json
import urllib
import os


while 1:
	# --- prepare file for data storage ------------------------------
	logFile_out = open("weatherLog.txt","a")
	# --- get weather information from from wunderground.com ---------
	response = urllib.urlopen("http://api.wunderground.com/api/ENTERYOURCODE/conditions/forecast/q/Germany/Celle.json")
	content = response.read()
	j = json.loads(content)

	# --- write header if file is read first time --------------------
	if os.path.getsize("weatherLog.txt") == 0L:
		headerString = "CurrDateTime; Temp; Humidity; Day0 ; Day0 Max Temp; Day0 Min Temp; Day0 Cond Txt; Day0 Cond Url; Day1 ; Day1 Max Temp; Day1 Min Temp; Day1 Cond Txt; Day1 Cond Url; Day2 ; Day2 Max Temp; Day2 Min Temp; Day2 Cond Txt; Day2 Cond Url; Day3 ; Day3 Max Temp; Day3 Min Temp; Day3 Cond Txt; Day3 Cond Url \n"
		logFile_out.write(headerString)

	# --- generate dataset and write to file -------------------------
	weatherString = str(j['current_observation']['observation_time_rfc822'])
	weatherString += ";	" + str(j['current_observation']['temp_c'])
	weatherString += ";	" + str(j['current_observation']['relative_humidity'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][0]['date']['weekday_short'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][0]['high']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][0]['low']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][0]['conditions'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][0]['icon_url'])

	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][1]['date']['weekday_short'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][1]['high']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][1]['low']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][1]['conditions'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][1]['icon_url'])

	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][2]['date']['weekday_short'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][2]['high']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][2]['low']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][2]['conditions'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][2]['icon_url'])

	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][3]['date']['weekday_short'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][3]['high']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][3]['low']['celsius'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][3]['conditions'])
	weatherString += ";	" + str(j['forecast']['simpleforecast']['forecastday'][3]['icon_url'])
	weatherString += "\n"
	logFile_out.write(weatherString)
	logFile_out.close()
	sleep(10)
