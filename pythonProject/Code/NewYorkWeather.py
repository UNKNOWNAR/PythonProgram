#nyc_weather.csv contains new york city weather for first few days in the month of
# January. Write a program that can answer following,
#What was the average temperature in first week of Jan
#What was the maximum temperature in first 10 days of Jan
from Code.HashMaps import HashMaps
class NewYorkWeather:
    def __init__(self):
        self.temp = []
    def load_file(self,file_path,HMaps):
        with open(file_path, "r") as f:
            for line in f:
                tokens = line.split(",")
                day = tokens[0]
                try:
                    temp = float(tokens[1])
                    self.temp.append(temp)
                    HMaps[day] = temp
                except Exception:
                    continue
    def avg_temp_week(self):
        total=0.0
        for temp in self.temp[:7]:
            total+= temp
        return (total/7)
    def maxm_temp(self):
        maxTemp = self.temp[0]
        for temp in self.temp:
            maxTemp = max(maxTemp,temp)
        return maxTemp
if __name__=="__main__":
    nycWeather = NewYorkWeather()
    HMaps = HashMaps()
    nycWeather.load_file("E:\\Python Folders\\pythonProject\\files\\nyc_weather.csv",HMaps)
    print(nycWeather.avg_temp_week())
    print(nycWeather.maxm_temp())
    print(HMaps.arr)
    print(HMaps["Jan 9"])