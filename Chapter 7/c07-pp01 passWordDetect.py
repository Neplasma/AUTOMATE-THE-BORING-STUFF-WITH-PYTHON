# Chapter 07 practice project 01
# Strong Password Detection
'''A strong password is defined as one
that is at least eight characters long,
contains both uppercase and lowercase characters,
and has at least one digit. '''

import re

text = '''niyuan5823
niyuanmike1
Niyuanmike1
Neptune
5823
Ny5823
NEPTUNE90
NepTune900501!'''

passWordRegex = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}')
# ?= means lookahead assertion
# .{8,} any charcter for at least 8 characters long 


matches = passWordRegex.findall(text)
print(matches)
