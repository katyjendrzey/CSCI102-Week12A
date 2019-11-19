# Katy Jendrzey
# Comp Sci 102 - Section E
# Week 12A - Utility

def PrintOutput(printprint):
    print('OUTPUT', printprint)

def LoadFile(filename):
    alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '
    alphabet = list(alphabet)
    filename = open(filename, 'r+')
    filename = filename.readlines()
    newoutput = list(filename)
    for val in range(0, len(newoutput)):
        for index in range(0, len(newoutput[val])):
            output = list(newoutput[val])
            if ''.join(output[index:index +1]) == '\n':
                del output[index:index + 1]
            newoutput[val] = ''.join(output)
    return newoutput
    
def UpdateString(x, y, z):
    x = list(x)
    newx = []
    for val in range(0, len(x)):
        if val != z:
            newx.append(x[val])
        else:
            newx.append(y)
    newx = ''.join(newx)
    PrintOutput(newx)

def FindWordCount(x, y):
    wordcount = 0
    for i in range(0, len(x)):
        if x[i] == y:
            wordcount += 1
    PrintOutput(wordcount)

def Union(x, y):
    newlist = []
    for i in range(0, len(x)):
        newlist.append(x[i])
    for j in range(0, len(y)):
        newlist.append(y[j])
    return newlist

def Intersection(x, y):
    finallist = []
    for i in range(0, len(x)):
        if x[i] in y:
            finallist.append(x[i])
    return finallist

def NotIn(x, y):
    finallist = []
    for i in range(0, len(x)):
        if x[i] not in y:
            finallist.append(x[i])
    return finallist

def ScoreFinder(x, y, z):
    x2 = []
    z2 = z.lower()
    existence = True
    for index in range(0, len(x)):
        x2.append(x[index].lower())
    if z2 not in x2:
        existence = False
    else:
        a = x2.index(z2)
    if existence == True:
        PrintOutput(f"{x[a]} got a score of {y[a]}")
    else:
        PrintOutput('player not found')
    
            
