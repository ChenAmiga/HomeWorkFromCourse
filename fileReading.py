import sys
try:
    N=int(input("הקלד מספר מילים נפוצות"))
except ValueError:
    raise Exception ("עליך להקליד מספר שלם")
if N<=0:
     raise Exception("עליך להקליד מספר חיובי")
content= sys.argv[1:]
dictC= {}
for i in range(len(content)):
    if content[i] in dictC:
        dictC[content[i]]=dictC[content[i]]+1
    else:
        dictC[content[i]]=1
sortedDict= sorted(dictC.items(), key=lambda item: item[1],reverse=True)
most= sortedDict[:N]
print (most)