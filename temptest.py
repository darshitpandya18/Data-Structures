abc = "A+B+c-d"
abc= abc.lower()
print(abc)


import re
abc1 = "Abcdaa"
print(re.match(abc1, '[a-zA-Z]'))