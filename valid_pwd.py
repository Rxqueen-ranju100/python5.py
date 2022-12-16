import re
passw = input("Enter Password ::>")
fl = 0
while True:
   if (len(passw)<8):
      fl= -1
      break
   elif not re.search("[a-z]", passw):
      fl = -1
      break
   elif not re.search("[A-Z]", passw):
        fl = -1
        break
   elif not re.search("[0-9]", passw):
      fl = -1
      break
   elif not re.search("[_@$#]", passw):
      fl = -1
      break
   elif re.search("\s", passw):
      fl = -1
      break
   else:
      fl = 0
      print(" This Is Valid Password")
      break
if fl ==-1:
   print("Not a Valid Password")
