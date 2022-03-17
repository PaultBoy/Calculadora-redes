import math
subIP1 = int(input("Introduce número: "))
binIP1 = []
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
print(binIP1Reversed)

