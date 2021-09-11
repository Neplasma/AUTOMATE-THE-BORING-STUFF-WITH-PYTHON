# Chapter 07 Practice Projects 02
# Regex Version of strip()

import re

text = '''      hello World         '''

def regexStrip(inP,inS): # inP = input text, inS = instruction
    if inS =='':
        textRegex = re.compile(r'^\s*|\s*$') # remove start and end of the string
    else:
        textRegex = re.compile(inS)

    output = textRegex.sub(r'',inP)
    print(output, inS + ' has been removed.')

regexStrip(text,'')
regexStrip(text,'e')
