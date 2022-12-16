import re
s='2002-12-26'
print('the date in format yyyy-mm-dd is :' +s)
t=(re.sub('2002-12-26','26-12-2002',s))
print('the date in format dd-mm-yyyy is :' +t)
