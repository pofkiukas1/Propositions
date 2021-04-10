import os

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

def chekem():
    return


vienasdidelissakyniumasyvas = readfile()
print(vienasdidelissakyniumasyvas)