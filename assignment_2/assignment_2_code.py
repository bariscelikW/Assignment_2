#global variables
myDatas = []
patProbabDic = {}
eachData = []
diseaseIncidence = []

#create function
def createFunc(textData):
    # splitting textData to two variables from space
    mainKey, otherKeys = textData.split(" ",1)
    # splitting otherKeys to create a list like: ['Hayriye', '0.999', 'Breast Cancer', '50/100000', 'Surgery', '0.40']
    eachData = otherKeys.split(", ")
    #checking data and if there is not in the myDatas: add it
    if eachData not in myDatas:
        myDatas.append(eachData)
        f.write("Patient {name} is recorded\n".format(name = eachData[0]))
    else:
        f.write("Patient {name} cannot be recorded due to duplication\n".format(name = eachData[0]))

#probability function
def probabilityFunc(textData):
    # splitting textData to two variables from space
    mainKey, otherKeys = textData.split(" ",1)
    # If otherKeys not in the list of names do this
    #namesOfList is a function to obtain names from data
    if otherKeys  not in namesOfList(myDatas):
        f.write("Probability for {name} cannot be calculated due to absence.\n".format(name = otherKeys))
    # find the true index and calculate the probability and create a dictionary, that's keys include names, and values include probability
    else:
        for i in range(len(myDatas)):
            if myDatas[i][0] == otherKeys:
                diseaseIncidence = myDatas[i][3].split("/")
                diagnosisAccuracy = myDatas[i][1]
                patProbabDic[myDatas[i][0]] = 100 * (int(diseaseIncidence[0]) / ((int(diseaseIncidence[1]) * (100 - (float(diagnosisAccuracy)*100)) / 100) + int(diseaseIncidence[0])))
                f.write("Patient {} has a probability of {:.2f}%  of having {}.\n".format(otherKeys, patProbabDic[myDatas[i][0]],  myDatas[i][2].lower()))

#recommendation function    
def recommendationFunc(textData):
        mainKey, otherKeys = textData.split(" ",1)
        #check and add namesofList function ?
        # I need to calculate the probabilities the person who is not applied the probability function before(it is not clean code, check it later)
        for i in range(len(myDatas)):
            if myDatas[i][0] == otherKeys:
                diseaseIncidence = myDatas[i][3].split("/")
                diagnosisAccuracy = myDatas[i][1]
                patProbabDic[myDatas[i][0]] = 100 * (int(diseaseIncidence[0]) / ((int(diseaseIncidence[1]) * (100 - (float(diagnosisAccuracy)*100)) / 100) + int(diseaseIncidence[0])))
        # I search the name in the patProbabDic and  if there is not here:
        if otherKeys not in patProbabDic.keys():
                f.write("Recommendation for {name} cannot be calculated due to absence\n".format(name = otherKeys))
        # if there is: 
        else:
            for i in range(len(myDatas)):
                # I compared the probability value and treatment risk
                if myDatas[i][0] == otherKeys and (float(myDatas[i][-1]) * 100) >  int(patProbabDic[otherKeys]):
                    f.write("System suggests {name} NOT to have the treatment.\n".format(name = otherKeys))
                elif myDatas[i][0] == otherKeys and (float(myDatas[i][-1]) * 100) <  int(patProbabDic[otherKeys]):
                    f.write("System suggests {name} to have the treatment.\n".format(name = otherKeys))
#remove function
def removeFunc(textData):
        mainKey, otherKeys = textData.split(" ",1)
        # If otherKeys not in the list of names do this
        #namesOfList is a function to obtain names from data
        if otherKeys not in namesOfList(myDatas):
            f.write("Patient {name} cannot be removed due to absence.\n".format(name = otherKeys))
        else:
            # removing data from correct index
            for i in range(len(myDatas)):
                if myDatas[i][0] == otherKeys:
                    myDatas.pop(i)
                    f.write("Patient {name} is removed.\n".format(name = otherKeys))
                    break
# listing function
def listingFunc(textData):
    mainKey = textData
    #-13s's mean is align it 13 character from the left side the page , - means from left
    f.write("%-13s %-10s %-17s %-13s %-15s %-13s\n"%("Patient", "Diagnosis", "Disease", "Disease", "Treatment", "Treatment"))
    f.write("%-13s %-10s %-17s %-13s %-15s %-13s\n"%("Name", "Accuracy", "Name", "Incidence", "Name", "Risk"))
    f.write("------------------------------------------------------------------------------------\n")
    # printing each elements from myDatas
    for i in range(len(myDatas)):
        f.write("%-13s  %-10s  %-17s  %-13s  %-15s  %-13s\n"%(myDatas[i][0], str(float(myDatas[i][1]) * 100)+'%', myDatas[i][2], myDatas[i][3], myDatas[i][4], str(float(myDatas[i][5]) * 100)+ '%'))

# to obtain names and create list
def namesOfList(list):
    namesData = []
    for name in list:
        namesData.append(name[0])
    return namesData

# read the input file and write the output file 
file = open("doctors_aid_inputs.txt", 'r')
f = open("my_output_file.txt", 'w')

# reading lines one by one
for line in file:
    line = line.strip()
    # checked the first line and do correct statement
    if line.startswith("create"):
        createFunc(line)

    if line.startswith("probability"):
       probabilityFunc(line)

    if line.startswith("recommendation"):
        recommendationFunc(line)
       
    if line.startswith("list"):
        listingFunc(line)

    if line.startswith("remove"):
        removeFunc(line)

f.close()