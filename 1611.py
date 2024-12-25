# students=[
#     ["Ваня","Полина","Настя","Таня"],
#     ["Степа","Максим","Саша",],
#     ["Дима","Игорь","Ксюша"]
# ]
# i=1
# for clas in students:
#     for name in clas:
#         print(f"Ученик - {name},класс - {i}")
#     i+=1
#

# for i, clas in enumerate(students,start = 1):
#     for name in clas:
#         print(f"Ученик - {name},класс - {i}")



matrix=[
    [5,1,3,2],
    [1,7,4,0],
    [1,3,6,1]

]
for row in matrix:
    for i in range(len(row)):
        row[i]*=2

print(matrix)



max_numb=matrix[0][0]
for row in matrix:
    for number in row:
        if number > max_numb:
            max_numb = number
print(f"Максимальное число - {max_numb}")



