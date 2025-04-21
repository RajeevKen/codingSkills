'''
{1: {'net_change': 60, 'net_change_percent': 222.22, 'reference_date': '2023-07-13', 'risk_score': 87},
2: {'net_change': 10, 'net_change_percent': 58.82, 'reference_date': '2023-07-12', 'risk_score': 27},
3: {'net_change': 17, 'net_change_percent': 17, 'reference_date': '2023-07-11', 'risk_score': 17}}
'''

'''
{'2023-07-11': {'net_change': 17, 'net_change_percent': u'17.00', 'risk_score': 17},
'2023-07-12': {'net_change': 10, 'net_change_percent': u'58.82', 'risk_score': 27},
'2023-07-13': {'net_change': 60, 'net_change_percent': u'222.22', 'risk_score': 87}}
'''

oldData = {1: {'net_change': 60, 'net_change_percent': 222.22, 'reference_date': '2023-07-13', 'risk_score': 87},
           2: {'net_change': 10, 'net_change_percent': 58.82, 'reference_date': '2023-07-12', 'risk_score': 27},
           3: {'net_change': 17, 'net_change_percent': 17, 'reference_date': '2023-07-11', 'risk_score': 17}}


     
def create_new_data(oldData):
    '''
    '''
    newData = {}
    temp = {}

    # oldData= {}
    for keys , values in oldData.items():
        for k, v in values.items():
            if k !='reference_date':
                # temp = oldData
                newData[v] = values
            # elif k =='reference_date':
            #     newData[v] = temp
            # newData[]

    print(newData)


create_new_data(oldData)



dict = {}

dict2 = {1 : 'a', 2: 'b'}

dict["new"] = dict2

# print(dict)