import re

x = 'sat mat cat rat bat '

txt = re.findall(r'[smr]at',x)
print(txt)
