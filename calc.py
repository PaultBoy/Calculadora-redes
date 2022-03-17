import math
ip = input("Introduce una IP: ")
mask = input("Introduce la máscara de subred: ")
ip=list(ip)
dotPos = []
for i in range(len(ip)):
    if ip[i] == ".":
        dotPos.append(i)

subIP1 = ip[0:dotPos[0]]
subIP2 = ip[dotPos[0]+1:dotPos[1]]
subIP3 = ip[dotPos[1]+1:dotPos[2]]
subIP4 = ip[dotPos[2]+1:len(ip)]

subIP1=''.join(subIP1)
subIP2=''.join(subIP2)
subIP3=''.join(subIP3)
subIP4=''.join(subIP4)
subIP1=int(subIP1)
subIP2=int(subIP2)
subIP3=int(subIP3)
subIP4=int(subIP4)

binIP1= []
while subIP1 / 2 >= 1:
    binIP1.append(subIP1 % 2)
    subIP1=subIP1/2
binIP1.append(1)
binIP1Corrected= []
for i in binIP1:
    i = math.floor(i)
    binIP1Corrected.append(i)
binIP1Reversed = []
for j in range(len(binIP1Corrected)):
    binIP1Reversed.append(binIP1Corrected[len(binIP1Corrected)-1-j])
for k in range(len(binIP1Reversed),8):
    binIP1Reversed.insert(0,0)

binIP2= []
while subIP2 / 2 >= 1:
    binIP2.append(subIP2 % 2)
    subIP2=subIP2/2
binIP2.append(1)
binIP2Corrected= []
for i in binIP2:
    i = math.floor(i)
    binIP2Corrected.append(i)
binIP2Reversed = []
for j in range(len(binIP2Corrected)):
    binIP2Reversed.append(binIP2Corrected[len(binIP2Corrected)-1-j])
for k in range(len(binIP2Reversed),8):
    binIP2Reversed.insert(0,0)

binIP3= []
while subIP3 / 2 >= 1:
    binIP3.append(subIP3 % 2)
    subIP3=subIP3/2
binIP3.append(1)
binIP3Corrected= []
for i in binIP3:
    i = math.floor(i)
    binIP3Corrected.append(i)
binIP3Reversed = []
for j in range(len(binIP3Corrected)):
    binIP3Reversed.append(binIP3Corrected[len(binIP3Corrected)-1-j])
for k in range(len(binIP3Reversed),8):
    binIP3Reversed.insert(0,0)

binIP4= []
while subIP4 / 2 >= 1:
    binIP4.append(subIP4 % 2)
    subIP4=subIP4/2
binIP4.append(1)
binIP4Corrected= []
for i in binIP4:
    i = math.floor(i)
    binIP4Corrected.append(i)
binIP4Reversed = []
for j in range(len(binIP4Corrected)):
    binIP4Reversed.append(binIP4Corrected[len(binIP4Corrected)-1-j])
for k in range(len(binIP4Reversed),8):
    binIP4Reversed.insert(0,0)

mask=list(mask)
dotPosMask = []
for i in range(len(mask)):
    if mask[i] == ".":
        dotPosMask.append(i)

subMask1 = mask[0:dotPosMask[0]]
subMask2 = mask[dotPosMask[0]+1:dotPosMask[1]]
subMask3 = mask[dotPosMask[1]+1:dotPosMask[2]]
subMask4 = mask[dotPosMask[2]+1:len(mask)]

subMask1=''.join(subMask1)
subMask2=''.join(subMask2)
subMask3=''.join(subMask3)
subMask4=''.join(subMask4)
subMask1=int(subMask1)
subMask2=int(subMask2)
subMask3=int(subMask3)
subMask4=int(subMask4)

binMask1= []
while subMask1 / 2 >= 1:
    binMask1.append(subMask1 % 2)
    subMask1=subMask1/2
binMask1.append(1)
binMask1Corrected= []
for i in binMask1:
    i = math.floor(i)
    binMask1Corrected.append(i)
binMask1Reversed = []
for j in range(len(binMask1Corrected)):
    binMask1Reversed.append(binMask1Corrected[len(binMask1Corrected)-1-j])
for k in range(len(binMask1Reversed),8):
    binMask1Reversed.insert(0,0)

binMask2= []
while subMask2 / 2 >= 1:
    binMask2.append(subMask2 % 2)
    subMask2=subMask2/2
binMask2.append(1)
binMask2Corrected= []
for i in binMask2:
    i = math.floor(i)
    binMask2Corrected.append(i)
binMask2Reversed = []
for j in range(len(binMask2Corrected)):
    binMask2Reversed.append(binMask2Corrected[len(binMask2Corrected)-1-j])
for k in range(len(binMask2Reversed),8):
    binMask2Reversed.insert(0,0)
binMask3= []
while subMask3 / 2 >= 1:
    binIP3.append(subMask3 % 2)
    subMask3=subMask3/2
binMask3.append(1)
binMask3Corrected= []
for i in binMask3:
    i = math.floor(i)
    binMask3Corrected.append(i)
binMask3Reversed = []
for j in range(len(binMask3Corrected)):
    binMask3Reversed.append(binMask3Corrected[len(binMask3Corrected)-1-j])
for k in range(len(binMask3Reversed),8):
    binMask3Reversed.insert(0,0)

binMask4= []
while subMask4 / 2 >= 1:
    binMask4.append(subMask4 % 2)
    subMask4=subMask4/2
binMask4.append(1)
binMask4Corrected= []
for i in binMask4:
    i = math.floor(i)
    binMask4Corrected.append(i)
binMask4Reversed = []
for j in range(len(binMask4Corrected)):
    binMask4Reversed.append(binMask4Corrected[len(binMask4Corrected)-1-j])
for k in range(len(binMask4Reversed),8):
    binMask4Reversed.insert(0,0)


dirRed1 = []
dirRed2 = []
dirRed3 = []
dirRed4 = []
for i in range(len(binIP1Reversed)):
    dirRed1.append(binIP1Reversed[i]*binMask1Reversed[i])
    dirRed2.append(binIP2Reversed[i]*binMask2Reversed[i])
    dirRed3.append(binIP3Reversed[i]*binMask3Reversed[i])
    dirRed4.append(binIP4Reversed[i]*binMask4Reversed[i])
print(binIP1Reversed, binIP2Reversed, binIP3Reversed, binIP4Reversed)
print(binMask1Reversed, binMask2Reversed, binMask3Reversed, binMask4Reversed)
print(dirRed1, dirRed2, dirRed3, dirRed4)