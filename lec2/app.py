import requests
import json
import time



data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')
# print(data.content)


# Json -> dic
dic = json.loads(data.content)

# print(dic)
# print(dic)

# 특정 시간 종가
print(dic['data'][0]['Close'])
print(dic['data'][1]['Close'])


# 반복문
for item in dic['data']:
  print('종가',item['Close'])
  format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(item['DT'])/1000))
  print('시간',format_time)


# time
# print('time',dic['data'][0]['DT'])

# time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch시간형식)) 
a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1739142000000/1000))
# print(a)  # 2025-02-10 08:00:00














