def funReadFromFilepath(pathToFile):
    file = open(pathToFile, 'r', encoding='utf8')
    fileText = file.read()
    file.close()
    return fileText

def funReadFromFile(pathToFile):
    file = open(pathToFile, 'r', encoding='utf8')
    fileText = file.read()
    file.close()
    funArray = fileText.split('<!>')
    del funArray[-1]
    #Ucinanie znaku \n z każdego elementu
    for x in range(len(funArray)):
        if funArray[x][:1] == '\n':
            funArray[x] = funArray[x][1:]
    return funArray

def funAddDataToFile(pathToFile, data):
    with open(pathToFile, 'a', encoding='utf-8') as a_file:
        a_file.write("\n")
        a_file.write(data+"<!>")
        a_file.close()

def funDeleteElementFromFlie(pathToFile, dataToDelete):
    file = open(pathToFile, 'r', encoding='utf=8')
    fileText = file.read()
    file.close()
    funArray = fileText.split('<!>')
    for x in range(len(funArray)):
        if funArray[x] == "\n"+dataToDelete or funArray[x] == dataToDelete:
            del funArray[x]
            break
    del funArray[-1]
    file = open(pathToFile, 'w', encoding='utf-8')
    for x in range(len(funArray)):
        file.write(funArray[x]+"<!>")

def funReadServiceFromFile(pathToFile):
    file = open(pathToFile, 'r', encoding='utf-8')
    fileText = file.read()
    file.close()
    ArrayOfNameAndUnit = fileText.split('<!>')
    del ArrayOfNameAndUnit[-1]
    #Ucinanianie znaku \n z każdego elementu
    for x in range(len(ArrayOfNameAndUnit)):
        if ArrayOfNameAndUnit[x][:1] == '\n':
            ArrayOfNameAndUnit[x] = ArrayOfNameAndUnit[x][1:]
    ArrayOfNameAndUnit.sort(key=str.lower)
    ArrayIdNameUnit = []
    for x in range(len(ArrayOfNameAndUnit)):
        strOfNameUnit = str(ArrayOfNameAndUnit[x]).split('<!!>')
        name = strOfNameUnit[0]
        unit = strOfNameUnit[1]
        fncKrotka = (str(x+1) + "     " + name + "     " + unit)
        ArrayIdNameUnit.append(fncKrotka)
    #Tablica wygląda następująco:
    #[x][0] - ID  [x][1] - nazwa   [x][2] - jednostka
    return ArrayIdNameUnit

def funAddServiceToFile(pathToFile, name, unit):
    with open(pathToFile, 'a', encoding='utf-8') as a_file:
        a_file.write("\n")
        a_file.write(name + "<!!>" + unit + "<!>")
        a_file.close()

def funDeleteServiceFromFile(pathToFile, name, unit):
    file = open(pathToFile, 'r', encoding='utf=8')
    fileText = file.read()
    file.close()
    funArray = fileText.split('<!>')
    for x in range(len(funArray)):
        if funArray[x] == "\n"+name+"<!!>"+unit or funArray[x] == name+"<!!>"+unit:
            del funArray[x]
            break
    del funArray[-1]
    file = open(pathToFile, 'w', encoding='utf-8')
    for x in range(len(funArray)):
        file.write(funArray[x] + "<!>")

def funReadLine(pathToFile):
    file = open(pathToFile, 'r', encoding='utf=8')
    fileText = ""
    fileText = file.readline()
    file.close()
    return fileText