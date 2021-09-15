# ITP Week 3 Day 3 Solution

## GET THE DATA
## CLEAN THE DATA
## LOOP THROUGH THE DATA
## OUTPUT THE DATA


import requests
import json
import openpyxl
from openpyxl.styles import Font

# using the requests package, we can make API calls to retrieve JSON
# and storing it into a variable here called "response"
response = requests.get("https://rickandmortyapi.com/api/character")

# verify the response status as 200
# print(response)

# verify the raw string data of the response
# print(response.text)

# load as a python json object and store into a variable called "clean_data"
clean_data = json.loads(response.text)

# print(clean_data)

# go through the results,
result = clean_data["results"]

# print(result[0])
# print(result[0]['location']['name'])

# first_item = result[0]
# print(type(first_item))  # disctionary
# print(first_item)
# print(first_item["name"])


wb = openpyxl.load_workbook("./input.xlsx")
sheet = wb['Sheet1']

sheet['A1'] = "Name"
# sheet['A1'].font = Font(bold = True)
sheet['B1'] = "Species"
# sheet['B1'].font = Font(bold = True)
sheet['C1'] = "Gender"
# sheet['C1'].font = Font(bold = True)
sheet['D1'] = "Location"
# sheet['D1'].font = Font(bold = True)

header_list = [sheet['A1'], sheet['B1'], sheet['C1'], sheet['D1']]

for header in header_list:
    header.font = Font(bold = True)

counter = 2
# for each row in an excel spreadsheet
for char in result:
    # print("Name: " + char['name'])
    sheet['A' + str(counter)] = char['name']

    # print("Species: " + char['species'])
    sheet['B' + str(counter)] = char['species']

    # print("Gender: " + char["gender"])
    sheet['C' + str(counter)] = char['gender']

    # print("Location: " + char['location']['name'])
    sheet['D' + str(counter)] = char['location']['name']
    counter+=1
# grab the name, species, gender, location name

# row = 1
# for character in result:
#     sheet['A' + str(row)] = character['name']
#     sheet['B' + str(row)] = character['species']
#     sheet['C' + str(row)] = character['gender']
#     sheet['D' + str(row)] = character['location']['name']
#     row += 1


wb.save('./output.xlsx')