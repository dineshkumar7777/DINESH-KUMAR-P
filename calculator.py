def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):   
   return x % y
def greaterthan(x, y):   
   return x > y
def leserthan(x, y):
   return x < y   
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.modulus")
print("6.greaterthan")
print("7.lesserthan")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1,"%",num2,"=", modulus(num1,num2))
elif choice =='6':
   print(num1,">",num2,"=",greaterthan(num1,num2)) 
elif choice =='7':   
   print(num1,"<",num2,"=",lesserthan(num1,num2)) 
else:
   print("Invalid input")
