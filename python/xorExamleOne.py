'''
Write a Python function to verify that a list of integers is sorted. 
If not, print the first occurrence of the unsorted pair.
 
example_list1 = [1, 2, 3, 4, 5] 
example_list2 = [1, 3, 2, 4, 5]
'''

def check_sort(loe):
    '''
    '''
    try:
        # loe = []
        sorted = loe
        elemA = ''
        elemB = ''
        for x in range(len(loe) -1):
            elemA = loe[x]
            elemB = loe[x+1]
            if elemA > elemB:
                print(f'List is not Sorted logging unsorted pair {loe[x]} {loe[x+1]}')
                break
            elif elemA < elemB:

                print(f'List is Sorted')
                
    except Exception as Error:
        raise Error


example_list1 = [1, 2, 3, 4, 5] 
example_list2 = [1, 3, 2, 4, 5]
check_sort(example_list1)