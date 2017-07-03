import _pickle as cPickle
mydict=dict()
with open("processed_tuples.pkl", "wb") as f:
    cPickle.dump(mydict, f)
print(mydict.pop())
data=cPickle.load(open("processed_tuples.pkl","rb"))
output = open("rocessed_tuples_Vahab.txt", "w")
output.write(str(data))
output.flush()
output.close()

'''''
file=open("rocessed_tuples_Vahab.txt", "r")
for line in file:
    lines=line.split()
    print(lines[3].)
'''''