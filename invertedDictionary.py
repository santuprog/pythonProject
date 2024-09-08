def buildInvDic(dict1):
    invDict={}
    for key,value in dict1.items():
        if value in invDict:
            invDict[value].append(key)
        else:
            invDict[value]=[key]
    invDict={x:invDict[x] for x in invDict if len(invDict[x])>1}
    return invDict

def main():
        wordMeaning=eval(input('Enter word meaning dictionary: '))
        meaningword=buildInvDic(wordMeaning)
        print('Inverted Dictionary:\n', meaningword)

if __name__ == '__main__':
    main()