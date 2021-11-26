# Chapter 07 practice question 20
# display digits with the corret comma group

import re

num1 = '1,234,567,899'
num2 = '1,234'
num3 = '1234'
num4 = '12'
num5 = '12,34'
num6 = '123'
num7 = '12,345'

def transDigit(text):
    digitRegex = re.compile(r'^((\d{1,3})(\,\d{3})*?$)')
    #digitRegex = re.compile(r'^100$|^[0-9]{1,2}$|^[0-9]{1,2}\,[0-9]{1,3}$')
    
   
    
    matches = []
    matches = digitRegex.findall(text)
    
    '''
    for groups in digitRegex.findall(text):
        if groups != '':
            matches+= groups '''
        
    if len(matches)>0:
        print(matches[0][0])
    else:
        print('Not Found')
    
    

transDigit(num1)
transDigit(num2)
transDigit(num3)
transDigit(num4)
transDigit(num5)
transDigit(num6)
transDigit(num7)
    
