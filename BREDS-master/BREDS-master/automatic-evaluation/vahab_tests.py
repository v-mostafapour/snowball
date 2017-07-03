import re
from nltk import word_tokenize

# entity = ". Sentence boundary disambiguation (SBD), also known as sentence breaking, is the";
sentence = ". Sentence boundary disambiguation (SBD), < also>  known as sentence breaking, </ is the >";
parts = word_tokenize(sentence)
entities = []
for m in re.finditer('\w', sentence):
    entities.append(m)
print("etities= ", entities)

print(map(lambda x: x.group(), re.finditer(r'\w', 'http://www.hackerrank.com/')))
if parts[-1] == '.':
    replace = parts[-2] + parts[-1]
    del parts[-1]
    del parts[-1]
    parts.append(replace)
print("parts=", parts)
regex_clean_simple = re.compile('</?[A-Z]+>', re.U)
regex_simple = re.compile('<[A-Z]+>[^<]+</[A-Z]+>', re.U)

print(regex_clean_simple)
print(regex_simple)
entities_regex = regex_simple
entities = []
for m in re.finditer(entities_regex, sentence):
    print("m=", m.groups())
    entities.append(m)
print(entities)

s = """xxxxx
Hello spam is my job hahaha!
Hello Python!
yyyyy"""

# match = re.search(r'^Hello (.*)$', s, re.MULTILINE)

for m in re.finditer(r'^Hello (.*)', s, re.MULTILINE):
    print(m.groups())
