import requests
url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
response = requests.get(url)
body = response.json()
price = []
for i in body:
    price.append(i['Cur_Name'])
print(price)
