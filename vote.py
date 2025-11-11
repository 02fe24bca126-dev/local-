try:
  a=int(input("enter age"))
  if age>=18:
    print("eligible")
  else:
    print("not eligible")
except valueError:
  print("enter valid integer age")
