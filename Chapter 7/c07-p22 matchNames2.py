# Chaptr 07 Practice Question 22
# matches people with given name of Alice, Bob, or Carol

import re

text = '''• 'Alice eats apples.'
• 'Bob pets cats.'
• 'Carol throws baseballs.'
• 'Alice throws Apples.'
• 'BOB EATS CATS.' but not the following:
• 'RoboCop eats apples.'
• 'ALICE THROWS FOOTBALLS.'
• 'Carol eats 7 cats.' '''

nameRegex = re.compile(r'''(
    (Alice|Bob|Carol)
    \s
    (eats|pets|throws)
    \s
    (apples|cats|baseballs)
    \.
    )''',re.VERBOSE | re.I)

matches = nameRegex.findall(text)
for i in range(len(matches)):
    print(matches[i][0])
