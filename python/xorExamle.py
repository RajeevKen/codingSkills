import difflib
import json 

dic = {'a':1, 'b':2,'c':3}

dicTwo = {'b':2, 'c':3, 'd':4}

# unique key value pairs


def check_unique_pairs(dic, dicTwo):
    """
    """
    try:
        d2 = {}
        diff = difflib.diff_bytes(dic, dicTwo,4)
        print(diff)
        # for k, v in dic.items():
        #     if dicTwo.__contains__(k):
        #         pass
        #     else:
        #         print(k,v)
        
    except Exception as error:
        raise error
    
check_unique_pairs(dic, dicTwo)



# second program



ls = [0,1,3,5,8,13,21,34,55]


def check_fibo(ls):
    """
    """
    index_one = ''
    index_two = ''
    
    for x in range(len(ls)-3):
        if ls[0]==0:
            index_one = ls[x]
            index_two = ls[x+1]
            if (index_one+index_two) != ls[x+2]:
                print('missing number is ',index_one+index_two )
                if (index_one+index_two)+index_two != ls[x+3]:
                    print('missing number',(index_one+index_two)+index_two)
                    break

        else:
            print("It should start with Zero, missing Zero")
            break
            


check_fibo(ls)