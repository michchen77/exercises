import requests,time

# 连接天气API
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
# 获取城市列表
print("正在载入")
url = "https://cdn.heweather.com/china-city-list.csv"
strhtml = requests.get(url,headers = headers)
strhtml.encoding = 'utf8'
data = strhtml.text
data1 = data.split('\r')
for c in range(2):
    data1.remove(data1[0])

class weather():
    def __init__(self,loco,cid=None):
        self.loco = loco
        self.cid = cid

    # 城市查找
    def search_city(self):
        for item in data1:
            city_list = item.split(',')
            if city_list[2] == self.loco or city_list[1] == self.loco:
                self.cid = city_list[0]
                print("城市查找成功，正在咨询天气")
                return self.weather_search()
            else:
                continue
        else:
            return False


    #天气查询
    def weather_search(self):
        url = "https://free-api.heweather.com/s6/weather/forecast?location=" + self.cid + "&key=1496dfc50bf746628c979c9351d9f51b"
        strhtml = requests.get(url, headers=headers)
        strhtml.encoding = 'utf8'
        time.sleep(1)
        dic = strhtml.json()
        result = "今日",dic['HeWeather6'][0]['update']['loc'],dic['HeWeather6'][0]['basic']['location'],'最高温度',dic['HeWeather6'][0]['daily_forecast'][0]['tmp_max'],'最低温度',dic['HeWeather6'][0]['daily_forecast'][0]['tmp_min']
        print(result)
        return True


if __name__ == "__main__":
    while True:
        loco = input("请输入要查询的城市")
        ws = weather(loco)
        if ws.search_city():
            break
        else:
            print('查询失败')
            ws.search_city()
    print("查询完成")