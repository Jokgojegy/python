import re

s = 'adc,acc,adc,afc,ahc'

r = re.findall('a[c-f]', s)
print(r)
