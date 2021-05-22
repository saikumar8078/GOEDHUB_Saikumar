colors = ['green','yellow','white','black']
fruits = ['apple','papaya','mango','orange']
animals = ['tiger','lion','deer','zebra']
word = input("enter any name of animal/plant/fruits ")
if word in colors:
    print(word+" is a color")

elif word in fruits:
    print(word+ " is a fruit")
else:
    print(word+"is a animal")



#part 2 question 1

country = ['alwal','hyd','secunderabad','mumbai','bandra','mahim','ooty','mysore']
a  = input("enter 1st city ")
b  = input("enter 2nd city ")
if a in country and b in  country:
    print("both are same country")
else:
    print("both are not same country")