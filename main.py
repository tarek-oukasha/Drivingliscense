# create a variable named and take an input from the user
name = input("what is yppur name: ")
age = int(input("to be able to aquire a driver's liscense you have to be over 18, please write your age: "))

if age >= 17 :
    print(f"Hi {name} you are elegibale to get a drivers liscense as you are {age} years old ")
else :
    print(f"Hi {name} you are not elegibale to get a drivers liscense as you are {age} years old")