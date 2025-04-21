st = 'welcome to persystent'


def remove_duplicates(st):
    '''
    '''
    # st = ''
    varOne = ''  
    varTwo = ''  
    for x in st:
        count = st.count(x)
        if count == 1 :
            varOne += x

    print(varOne)


# remove_duplicates(st)


    #     varOne = st[x]
    #     varTwo = st[x+1]
    #     if 


# sort in desending
#  ar = [85, 64, 23, 14, 55, 75, 34, 45]

def sort_desending():
    '''
    '''
    ar = [85, 64, 23, 14, 55, 75, 34, 45]

    elem_one = ''
    elem_two = ''
    swap_elem = ''
    x = 0
    while x < len(ar):
        for ele in range(len(ar)-1):
            
            swap_elem = elem_one
            elem_one = ar[ele]
            elem_two = ar[ele+1]

            if elem_one < elem_two :
                ar[ele] = elem_two
                ar[ele+1] = elem_one
        x += 1
    return ar


print(sort_desending())

