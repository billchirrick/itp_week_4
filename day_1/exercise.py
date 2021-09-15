# ITP Week 4 Day 1 Exercise

# https://data.messari.io/api/v2/assets

import requests
import json
import openpyxl

wb = openpyxl.load_workbook("output.xlsx")
sheet = wb["Sheet1"]

def get_data(url):
    response = requests.get(url)
    # print(response)
    json_result = response.text
    # print(json_result)
    # print(type(json_result))
    clean_data = json.loads(json_result)
    result = clean_data["data"]
    return result

row = 1

def write_data(result):
    global row
    for messari in result:
        sheet['A' + str(row)] = messari['symbol']
        sheet['B' + str(row)] = messari['name']
        sheet['C' + str(row)] = messari['metrics']['market_data']['price_usd']
        row+=1


result_1 = get_data("https://data.messari.io/api/v2/assets")
result_2 = get_data("https://data.messari.io/api/v2/assets?page=2")
result_3 = get_data("https://data.messari.io/api/v2/assets?page=3")

write_data(result_1)
write_data(result_2)
write_data(result_3)
write_data(get_data("https://data.messari.io/api/v2/assets?page=4"))



wb.save("output.xlsx")