# ITP Week 4 Day 3 Lecture

# imports up top
import requests
import json
import openpyxl
import functions

pokemon_list = []

wb = openpyxl.Workbook()
sheet = wb.active

# sequence of commands
functions.make_header(sheet)
functions.populate_pokemon(requests, json, "https://pokeapi.co/api/v2/pokemon/", pokemon_list)
functions.populate_data(requests, json, pokemon_list)
wb.save("/home/dkayzee/vit/intro-python-august-2021/itp_week_4/day_3/output.xlsx")