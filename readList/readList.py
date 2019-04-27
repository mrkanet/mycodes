import csv
x_csv = open('readList.txt', mode="r")
reader = x_csv.read()

'''
#### Version 0.1

read = reader.split(",")

uriDizi=[]
ara = "\"spot" #ify:track:"
uzunluk = "\"spotify:track:1EYb9cZfx1d4qUswLnbfn1\"" #" "spotify:track:4nIDWcUZWDrERMIxV4eJTX" " 
uzunluk = len(uzunluk)

for i in range(5854): #diziyi tara
#print (read[i])
if uzunluk == len(read[i]): 
counter = 0
for j in range (len(ara)):
strin = read[i]
if strin[j] == ara[j]:
counter+=1
else:
break
if counter == len(ara):
uriDizi.append(strin[1:37])
elif len(read[i]) == 61:
counter = 0
for j in range (len(ara)):
strin = read[i]
if strin[j+23] == ara[j]:
counter+=1
else:
break
if counter == len(ara):
uriDizi.append(strin[24:60])

print(uriDizi) 
'''

##### Version 0.2

read = reader.split('\n')
uris=[]
for i in read:
uris.append(i[1:37])
print(uris)
