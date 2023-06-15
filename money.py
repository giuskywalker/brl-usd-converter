#!/bin/python3

from bs4 import BeautifulSoup
from datetime import date
import requests
import os

url_dollar = "https://www.xe.com/pt/currencyconverter/convert/?Amount=1&From=BRL&To=USD"
url_real = "https://www.xe.com/pt/currencyconverter/convert/?Amount=1&From=USD&To=BRL"
today = date.today()

while True:
    print ("""
 _______________________
|~ Possible operations ~|
|~ 1 - Dollar to real  ~|
|~ 2 - Real to dollar  ~|
|~ 3 - Quit            ~|
|_______________________|
""")
    choose = int(input("~: "))

    if choose == 1:
        page = requests.get(url_dollar)
        soup = BeautifulSoup(page.content, 'html.parser')
        value_locate = soup.find_all("div", class_="unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx")
        value = str(value_locate).split()
        comma_value = value[5]
        real_value = float(comma_value.replace(",", "."))
        print("")
        value2convert = float(input("How much you want to convert?: "))
        final_value = real_value * value2convert
        final_rounded = round(final_value, 2)
        print(f"$ {value2convert} USD are {final_rounded} BRL. $")
        print("")
        input("[press enter to continue]")
        os.system("clear")

    elif choose == 2:
        page = requests.get(url_real)
        soup = BeautifulSoup(page.content, 'html.parser')
        value_locate = soup.find_all("div", class_="unit-rates___StyledDiv-sc-1dk593y-0 dEqdnx")
        value = str(value_locate).split()
        comma_value = value[5]
        dollar_value = float(comma_value.replace(",", "."))
        print("")
        value2convert = float(input("How much you want to convert?: "))
        final_value = dollar_value * value2convert
        final_rounded = round(final_value, 2)
        print(f"$ {value2convert} BRL are {final_rounded} USD. $")
        print("")
        input("[press enter to continue]")
        os.system("clear")
    
    elif choose == 3:
        print("Goodbye :)")
        quit()
