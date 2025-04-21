'''
Write a Python program to find the longest consecutive sequence in an unsorted list
Input = [100, 4, 200, 1, 50, 3, 32, 2]
Output = 4, [1, 2, 3, 4]
'''

def checkSeq():
    '''
    '''
    # list_of_nums = []
    # list_of_nums.append(str(input('Enter the array of nums : ')).split(","))
    Input = [100, 4, 200, 1, 50, 3, 32, 2]
    Input.sort()
    strng = ''
    
    for num in range(len(Input)-1):
        strng += str(Input[num])+ " "

    print(strng)
checkSeq()


'''
Write a Python program to find the First Non-Repeating Number from array
Input = [1, 5, 10, 9, 1, 2, 5]
Output = [10]
'''
def nrn():
    '''
    '''
    Input = [1, 5, 10, 9, 1, 2, 5]
    dictn = {}
    # for num in range(len(Input)):
    for num in Input:
        if Input.count(num) == 1:
            dictn[num] = Input.count(num)
            break
    print(f'Number {dictn.keys()} is repeated {dictn.values()} times')

nrn()