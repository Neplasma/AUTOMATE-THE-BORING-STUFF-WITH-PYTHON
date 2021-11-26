#Chapter 06 Practice Table Printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
                          ['Alice', 'Bob', 'Carol', 'David'],
                          ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    x = len(table[0]) # get the no. of columns in matirx
    y = len(table) # get the no. of rows
    colWidths = [0]*y # the list to store max string lentgh in each row

    '''get the length of the longest string in each row
    and store them in colWidth'''
    for i in range(len(tableData)):
        colWidths[i]=len(max(tableData[i],key=len)) 

    # print out matrix with x and y swapped and right-just the margin
    # aligning with the longest string in the row
    for j in range(x):
        print('')
        for i in range(y):
            print(table[i][j].rjust(colWidths[i]+1,'•'),end=' ')

'''call the function'''
printTable(tableData)
    
    
    
            
    
