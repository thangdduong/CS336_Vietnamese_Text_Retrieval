import re

url = re.compile(r"www\S+")
url = url.sub('', 'www.google').strip().strip('/')

print(url)