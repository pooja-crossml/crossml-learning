#Dictonary comprehension
#sample={1:1,2:4,3:6} dictonary of squares

square={name:name**2 for name in range(1,11)}
#print(type(square))
square1 = {f"Square of {num}:{num**2}"for num in range(1,11)}
print(square1)
for k,v in square.items():
    print(f"{k}:{v}")

#for k,v in square1.items():
 #   print('k:v')

name="Pooja Rani"

char_count={cahr:name.count(cahr) for cahr in name}
print(char_count)




#if-else in dictonary comprehension

#d={1:'odd',2:'even'}

odd_even={i:('even ' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)




#Set comprehension


num={n**2 for n in range(1,11)}
print(num)

s={1,2,3,1}
print(s)
l=[1,2,3,4,5,6,1,2,3,4,6,7,8,9]

#remove duplicate
se=list(set(l))

print(se)
print(type(se))

#Get first caharcter from the string
names=['Lisa','Meera',"Pooja",'Harshit','Veena']
first_name={a[0] for a in names}
print(first_name)

# List examples

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for i in planets:
    print(i,end=" ")

square=[]
for i in range(5):
    square.append(i**2)
    print(square)

exp=('One',"Two",'Three')
print(exp)
print(exp[:2])



#Loops in tuple

mixed=(1,2,3,4,5,5.05)
for i in mixed:
    print(i,end=" ")
print("\n------------------------")
j=0
while j<len(mixed):
    print(mixed[j])
    j+=1