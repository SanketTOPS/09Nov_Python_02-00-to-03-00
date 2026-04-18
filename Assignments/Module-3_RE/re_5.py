import re

mystr="These is Pythson!"

#x=re.findall('Py..on',mystr)
x=re.findall('This|That',mystr)
print(x)