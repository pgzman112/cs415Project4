#Preston Zimmerman
#Diana Acre
#5/14/21
#Project4

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def MFKnapsack(i,j):
    #print("on i,j: ", i, " ", j)
    if contents2[i][j] < 0:
        if j < weightArray[i-1]:
            value = MFKnapsack(i-1, j)
        else:
            value = max(int(MFKnapsack(i-1,j)), int(valueArray[i-1] + MFKnapsack(i-1, j-weightArray[i-1])))
        contents2[i][j] = value
    return contents2[i][j]

fileCap = open('KnapsackTestData/p00_c.txt', 'r')
capacity = fileCap.readlines()
capacity = int(capacity[0])
print(capacity)
fileValues = open('KnapsackTestData/p00_v.txt', 'r')
values = fileValues.readlines()
fileWeights = open('KnapsackTestData/p00_w.txt', 'r')
weights = fileWeights.readlines()
fileWeights.close()
fileValues.close()
fileCap.close()
itemArray = []
weightArray = []
valueArray = []

for x in range(0, len(values), 1):
    itemArray.append(Item(int(values[x]), int(weights[x])))
    weightArray.append(int(weights[x]))
    valueArray.append(int(values[x]))
    #print("adding Item of v, w: ", itemArray[x].value, ", ", itemArray[x].weight)

#contents = [[0] * (1 + capacity)] * (len(itemArray)+1)

contents = [[0 for i in range(1+capacity)] for j in range(len(itemArray)+1)]
#contents = [[0 for i in range(len(values))]]
#print(contents)

for i in range(0, len(itemArray)+1, 1):
    if i == 0:
       #skip
       currentValue = 0
       currentWeight = 0
    else:
        currentValue = int(itemArray[i-1].value)
        currentWeight = int(itemArray[i-1].weight)

    for j in range(0, capacity+1, 1):
        #print(contents)
        if i == 0:
            contents[i][j] = 0
        else:
            #print(j-currentWeight)
            if (j-currentWeight) >= 0:
                #print("here on i,j: ", i, ", ", j)
                tempVal = int(currentValue + contents[i-1][j-currentWeight])
                #print(tempVal)
                #print(max(contents[i-1][j], tempVal))
                temp = int(max(contents[i-1][j], tempVal))
                contents[i][j] = temp
            else:
                temp = int(contents[i-1][j])
                contents[i][j] = temp

#print(contents)

print("optimal value: ", contents[len(itemArray)][capacity])
itemSubset = []
i = len(itemArray)
j = capacity
while contents[i][j] != 0:
    if contents[i][j] > contents[i-1][j]:
        #this means the current Item belongs in the final solution
        itemSubset.append(i)
        i = i - 1
        j = j - itemArray[i].weight
    else:
        #this mean current was not used so just decrement i
        i = i - 1
itemSubset.reverse()
print(itemSubset)


contents2 = [[-1 for i in range(1+capacity)] for j in range(len(itemArray)+1)]
#print(contents2)
for x in range(capacity+1):
    contents2[0][x] = 0
for y in range(len(itemArray)+1):
    contents2[y][0] = 0
#print(contents2)

#memFunk(len(itemArray), capacity, weightArray, contents2)
MFKnapsack(len(itemArray), capacity)
#print(contents2)

memItemSubset = []
i = len(itemArray)
j = capacity
while contents2[i][j] != 0:
    if contents2[i][j] > contents2[i-1][j]:
        #this means the current Item belongs in the final solution
        memItemSubset.append(i)
        i = i - 1
        j = j - itemArray[i].weight
    else:
        #this mean current was not used so just decrement i
        i = i - 1
memItemSubset.reverse()
print("optimal value: ", contents2[len(itemArray)][capacity])
print(memItemSubset)
