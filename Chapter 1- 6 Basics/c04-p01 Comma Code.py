#  Chapter 04 Practice Comma Code

def commaCode(aList): 
    for i in range(0,len(aList)-1):
        print(aList[i]+', ', end='')
    print(' and ' + aList[-1])
        
    
spam = ['apples', 'bananas', 'tofu', 'cats']
commaCode(spam)
