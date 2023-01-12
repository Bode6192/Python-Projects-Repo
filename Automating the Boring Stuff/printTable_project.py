tableData = [['apples', 'oranges', 'cherries', 'banana'], 
            ['Alice', 'Bob', 'Carol', 'David'], 
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidth = [0] * len(list)
    for string in list[0]:
        if len(string) > colWidth[0]:
            colWidth[0] = len(string)

    for string in list[1]:
        if len(string) > colWidth[1]:
            colWidth[1] = len(string)

    for string in list[2]:
        if len(string) > colWidth[2]:
            colWidth[2] = len(string)

    for j in range(len(list[0])):
        for i in range(len(list)):
            new_string = list[i][j] + ' '
            print(new_string.rjust(colWidth[i] + 2, ), end='')
        print()

printTable(tableData)


