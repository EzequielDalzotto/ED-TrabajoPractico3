import re


numeros = ["(0345) 154123456",
          "+5493454123456",
          "3454123456",
          "+54011123456",
          "34564123456"]

patron = "^(((3454)|(\\+5493454)|(\\(0345\\)\s(154)))\d{6})$"

for i in numeros:
    match = re.match(patron, i)
    if match:
        print(i);