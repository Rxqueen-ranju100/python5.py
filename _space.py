import re
p=re.compile(' ')
r=p.sub('_','hii how are you')
print(r)
c=re.compile('_')
d=c.sub(' ','hii_how_are_you')
print(d)
