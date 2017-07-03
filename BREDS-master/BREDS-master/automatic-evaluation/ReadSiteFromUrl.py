import re
import requests
import string
import urllib
import urllib.request
import urllib.request

"""""
response = requests.get('http://docs.python-requests.org/en/master/')
pattern = re.compile(b'<title>(,+?)</title>', re.M)
result = re.match(pattern, response.text)
title= pattern.match(response.text)
print(title.group(0))
print(response.text)

url1= "https://www.daniweb.com/programming/software-development/threads/332557/python-opening-a-html-file";
url2="http://www.google.com/ig?hl=en";

with urllib.request.urlopen(url1) as html:
    code = html.read()
    print("code= ",code)

pattern = re.compile(b'<title>(,+?)</title>', re.M)

title = re.findall(pattern, code)

print("title= ",title)

"""""
#stockname = input('Enter the stock name : ')
#az net: page = urllib.urlopen("your path ").read()
#url = "http://www.google.com/ig?hl=en"
url="http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string";
htmlfile = urllib.request.urlopen(url)
htmltext = htmlfile.read().decode('utf-8').strip()
regex = '<script>(,+?)'
pattern = re.compile(regex)
price = re.findall(pattern,htmltext)
print ("price=",price)


"""
You want to convert html (a byte-like object) into a string using .decode,
 e.g.  html = url.read().decode('utf-8').


with urllib.request.urlopen("http://www.python.org") as url:
    s = url.read().decode('utf-8')
#I'm guessing this would output the html source code?
print(s)

url ="http://www.python.org"# input('Please enter website URL : ')
with urllib.request.urlopen('http://steve-yegge.blogspot.com/2007/08/how-to-make-funny-talk-title-without.html') as html:
    code = html.read().decode('utf-8')

pattern = re.compile(r'<title>(,+?)</title>', re.M)

title = re.findall(pattern, code)

print(title)

print("%s title is : %s" ,(url, title))

html = urllib.urlopen('http://steve-yegge.blogspot.com/2007/08/how-to-make-funny-talk-title-without.html').read()
pattern = r'\b(the\s+\w+)\s+'
regex = re.compile(pattern, re.IGNORECASE)
for match in regex.finditer(html):
    print ("%s: %s" % (match.start(), match.group(1)))

"""