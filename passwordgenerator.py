import random
lst1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y", "z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lst2=[0,1,2,3,4,5,6,7,8,9]
lst3=["`","!","@","#","$","%","^","&","*","(",")","_","-","+","=",",","<",".",">","?","/","'",":",";","{","[","}","]"]
n=int(input("Enter the number of letters: "))
a=int(input("Enter the number of digits: "))
b=int(input("Enter the number of special characters: "))
password=""
for i in range(n):
    password+=str(random.choice(lst1))
for i in range(a):
    password+=str(random.choice(lst2))
for i in range(b):
    password+=str(random.choice(lst3))
print(f"Generated Password is: {password}")

