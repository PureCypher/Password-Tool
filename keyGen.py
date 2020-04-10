import random
import string

def randomPasswdMix(length):
    PuncDic = ["!","#","$","(",")",",",".",":",";","?","@","[","]","_","`","{","}","~"]
    list_key = []
    for r in range(length):
        list_key.append(random.randint(1,4))
    key = []
    for item in list_key:
        if item == 1:
            key.append(random.choice(string.ascii_lowercase))
        elif item == 2:
            key.append(random.choice(string.ascii_uppercase))
        elif item == 3:
            key.append(random.randint(0,9))
        elif item == 4:
            key.append(random.choice(PuncDic))
    lendd = len(key)
    return str(''.join(str(key[i]) for i in range(lendd)))

def randomPasswd(length):
    list_Passwd = []
    for r in range(length):
        list_Passwd.append(random.randint(1,3))
    key_Passwd = []
    for key in list_Passwd:
        if key == 1:
            key_Passwd.append(random.choice(string.ascii_lowercase))
        elif key == 2:
            key_Passwd.append(random.choice(string.ascii_uppercase))
        elif key == 3:
            key_Passwd.append(random.randint(0,9))
    lendd = len(key_Passwd)
    return str(''.join(str(key_Passwd[i]) for i in range(lendd)))

def randomWordPasswd(mix, leet):
    mixer = []
    count = len(open("words_alpha.txt", "r").readlines())
    for m in range(mix):
        word = open("words_alpha.txt", "r").readlines()[random.randint(0,count)]
        if leet == True:
            word = word.replace("a", "4")
            word = word.replace("e", "3")
            word = word.replace("i", "1")
            word = word.replace("o", "0")  
        mixer.append(word.strip())
    lendd = len(mixer)
    return str(''.join(str(mixer[i]) for i in range(lendd)))

def twoFactor(mix):
    randomFactor = []
    Factor = []
    if mix == True:
        for i in range(6):
            randomFactor.append(random.randint(1,3))
        for key in randomFactor:
            if key == 1:
                Factor.append(random.choice(string.ascii_lowercase))
            elif key == 2:
                Factor.append(random.choice(string.ascii_uppercase))
            elif key == 3:
                Factor.append(random.randint(0,9))
    elif mix == False:
        for i in range(6):
            Factor.append(random.randint(0,9))
    lendd = len(Factor)
    return str(''.join(str(Factor[i]) for i in range(lendd)))
