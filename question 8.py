marks_list = [65,75,2100,95,83]

#print(len(marks_list))
marks = int(input("enter marks "))
if marks in marks_list:
    print('test',marks_list.index(marks)+1)
else:
    print("well")