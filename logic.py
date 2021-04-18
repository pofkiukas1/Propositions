import os
from difflib import SequenceMatcher
def readfile():
    returnthis = []
    empty = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + '\propositions.txt') as f:
        content = f.readlines()
    for i in range(len(content)):

        empty = content[i].strip().split(" ")
        returnthis.append(empty)
    # print(content)
    return returnthis
vienasdidelissakyniumasyvas = readfile()
def reverse(a):
    masyvas = a.split()
    for i in range(len(masyvas)):
        if ("-") in masyvas[i]:
            masyvas[i] = masyvas[i].replace("-", "")
        else:
            masyvas[i] = "-" + masyvas[i]
    return masyvas

def doesitexistinlist(sakniys1,sakinys2):
    emptystring1 = ""
    emptystring2 = ""

    for x in sakniys1:
        emptystring1 = emptystring1 + x
    for x in sakinys2:
        emptystring2 = emptystring2 + x
    if all(item in sakinys2 for item in sakniys1):
        return True
    return False

def kandidatas(tikrinamas1, tikrinamas2):

    for i in range(len(tikrinamas1)):
        for j in range(len(tikrinamas2)):
            # print(tikrinamas1, tikrinamas2)
            # print("tikrinamas1[i] su tikrianamas2[j] ",tikrinamas1[i], " su ", tikrinamas2[j])
            if ("-") in tikrinamas1[i]:
                
                if ("-") in tikrinamas2[j]:
                    if tikrinamas1[i][1:] == tikrinamas2[j][1:]:
                        pass
                        # ta pati -raide
                else:
                    if tikrinamas1[i][1:] == tikrinamas2[j][0:]:
                        # SITA TINKA 
                        tempcopy1 = tikrinamas1.copy()
                        tempcopy2 = tikrinamas2.copy()
                        tempcopy1.pop(i)
                        tempcopy2.pop(j)

                        thisset = set()
                        thisset.update(tempcopy1)
                        thisset.update(tempcopy2)
                        returnthis = []
                        for x in thisset:
                            returnthis.append(x)
                        returnthis = prastinti(returnthis)
                        return returnthis

            elif ("-") in tikrinamas2[j]:
                if ("-") in tikrinamas1[i]:
                    if tikrinamas1[i][1:] == tikrinamas2[j][1:]:
                        pass
                        # ta pati -raide
                else:
                    if tikrinamas1[i][0:] == tikrinamas2[j][1:]:
                        # SITA TINKA 
                        tempcopy1 = tikrinamas1.copy()
                        tempcopy2 = tikrinamas2.copy()
                        tempcopy1.pop(i)
                        tempcopy2.pop(j)

                        thisset = set()
                        thisset.update(tempcopy1)
                        thisset.update(tempcopy2)
                        returnthis = []
                        for x in thisset:
                            returnthis.append(x)
                        returnthis = prastinti(returnthis)
                        return returnthis


def prastinti( logic):
    temp = logic.copy()
    ### ISVALO -B ir B 
    for x in temp:
        if temp.count(x) > 1:
            temp.remove(x)
        if x[0] == "-":
            if x[1:] in temp:
                return None
    logic = temp
    ###

    ###
    return logic

def arsilpnesnis(naujas,ZB):
    for x in ZB:
        if doesitexistinlist(x, naujas):
            return False
            
    return True

def loopui(i,testthis):
    if i < len(testthis):
        return True
    else:
        return False
def rezoliucija(ZB):
    naujisakiniai=[]
    print(len(ZB))
    counter = 0
    testthis = ZB.copy() # gali buti blogai
    # print(testthis)
    i = 1
    while loopui(i,testthis):
    # for i in range(1, len(testthis)):
        counter += 1
        for j in range(i-1, -1, -1):
            naujas = kandidatas(testthis[i],testthis[j])
            if naujas and naujas not in testthis and arsilpnesnis(naujas,testthis):
                testthis.append(naujas)
                stringas = ""
                for x in naujas:
                    stringas = stringas + x + " "
                stringas = stringas + " sk: "+ str(testthis.index(naujas)) + " " +str(i)+", " +str(j)
                naujisakiniai.append(stringas)
        i += 1
    print("nauji: ")
    for x in naujisakiniai:
        print(x)
    print(len(testthis))
                

    return vienasdidelissakyniumasyvas




print("pradiniai: ")
k = 0
for x in vienasdidelissakyniumasyvas:
    print(x," ", k)
    k += 1
rezoliucija(vienasdidelissakyniumasyvas)
