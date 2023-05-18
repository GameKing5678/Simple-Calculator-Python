c = input('Enter operator ( either +, -, * or / )\n')
a1 = input ('Enter first number: \n')
b1 = input ('Enter second number: \n')
a = float(a1)
b = float(b1)

if c == '+' :
  print("Your answer is",a+b) 

if c == '-' :
  print ("Your answer is", a-b)

if c == '*' :
  print ("Your answer is", a*b)

if c == '/' :
  print ("Your answer is ", a/b)
  
print ("Thanks for using simple calculator \nMade by Gameking5678")
