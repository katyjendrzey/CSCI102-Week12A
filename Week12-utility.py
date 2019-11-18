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
