def beautify(matrix):
    finalRes=0
    for row in range(5):
        for coloumn in range(5):
            if matrix[row][coloumn]=="1":
                rowToBeautify=abs(row-2)
                coloumnToBeautify=abs(coloumn-2)
                finalRes=rowToBeautify+coloumnToBeautify
    return finalRes


matrix=[]
for i in range(5):
    input_=input().split()
    matrix.append(input_)
print(beautify(matrix))
