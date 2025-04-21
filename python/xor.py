'''
Instructions:
1. Resolve errors
2. Print output as a5l1p1h1b1e1t1g1m2

s = "alphabetagamma"
sdict = {}
for character in s:
sdict[character] += 1
'''
from collections import Counter

def get_count():
    '''
    '''
    s = "alphabetagamma"

    data = Counter(s)
    newString = ''
    for keys , values in data.items():
        newString+= keys
        newString+= str(values)
    # print(newString)





    s = "alphabetagamma"
    sdict = {}
    for character in s:
        sdict[character] = s.count(character)

    # print(sdict)

get_count()


'''
a = input("Give me a number: ")
b = 10
if a < b:
  print("a is lesser than b")
elif a > b:
  print("a is greater than b")
else:
  print("a and b are equal”)
'''

def comValues():
    '''
    '''
    try:
        a = bool(input("Give me a number: "))
        # while
        #     a = int(input("Give me a number: "))
        b = 10.5
        if a < b:
            print("a is lesser than b")
        elif a > b:
            print("a is greater than b")
        else:
            print("a and b are equal")
    except Exception as Error:
        # raise Error
        print(Error)

# comValues()


class MarksOfStudent():
    '''
    '''
    def __init__(self):
        '''
        '''
        self.student_name = 'abc'
        self.student_marks = 78



class OverrideStudent(MarksOfStudent):
    '''
    '''
    def updated_marks(self):
        '''
        '''
        marks_u = ''
        # class_object = MarksOfStudent.marks
        self.student_marks = 80
        # self.student_name = 'xyz'
        print(self.student_marks)


OverrideStudent().updated_marks()