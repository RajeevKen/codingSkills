'''
Input string:”hello rajeev hello rajeev”
Output: {“hello”:[0,2] ,”rajeev”:[1,3]}
'''

from collections import Counter


def countElem():
    '''
    '''
    InputS = "hello rajeev hello rajeev"
    listOfItems = InputS.split(" ")
    print(Counter(listOfItems))
    dicItem = {}
    
    for elem in listOfItems:
        elemList = []
        stItem = ''
        for y in range(elem.count(elem)):
            # elemList.append(listOfItems.index(elem))
            stItem += str(listOfItems.index(elem))
            dicItem[elem] = list(stItem)

    for x, y in Counter(listOfItems).items():
        dicItem[x] = listOfItems.index(x)


    print(dicItem)

countElem()