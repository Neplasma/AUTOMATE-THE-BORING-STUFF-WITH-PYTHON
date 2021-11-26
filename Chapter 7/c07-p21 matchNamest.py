# Chaptr 07 Practice Question 21
# matches people with surename of Nakamoto

import re

text = '''• 'Satoshi Nakamoto'
• 'Alice Nakamoto'
• 'RoboCop Nakamoto' but not the following:
• 'satoshi Nakamoto' (where the first name is not capitalized)
• 'Mr. Nakamoto' (where the preceding word has a nonletter character)
• 'Nakamoto' (which has no first name)
• 'Satoshi nakamoto' (where Nakamoto is not capitalized)'''

nameRegex = re.compile(r'''(
    ([A-Z][A-Za-z]*[^.])
    (\s)
    Nakamoto
    )''',re.VERBOSE)

matches = nameRegex.findall(text)
for i in range(len(matches)):
    print(matches[i][0])


