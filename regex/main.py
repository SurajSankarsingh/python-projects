import re

pattern = re.compile('search this inside of this text please!')
string = 'search this inside of this text please! Dave'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(d)
