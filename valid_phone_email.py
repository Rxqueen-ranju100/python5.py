import re

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

Mobile = phoneRegex.search("my number is 123-456-6789")

print(Mobile.group())

def solve(E):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,E):
      return True
   return False

E = "raanjumb17@gmail.com"
print(solve(E))
