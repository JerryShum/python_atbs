# For practice, write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right- justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:

testTableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def printTable(tableData):
    stringsListPrint = []
    numRows = 0
    numCols = len(tableData)

    for dataList in tableData:
        numRows = len(dataList)
        longest = 0
        dataListString = []
        goodstring = ""
        for entry in dataList:
            if len(entry) > longest:
                longest = len(entry)

        # you have the longest value in the list --> rjust()
        for entry in dataList:
            formatted = entry.rjust(longest)
            dataListString.append(formatted)

        stringsListPrint.append(dataListString)

    print(stringsListPrint)
    # loop through the rows and the columns
    for row in range(numRows):
        # we are building the rows of the columns
        rowString = ""
        for col in range(numCols):
            # append the 1st value of each column (thats how you build out a row)
            rowString += stringsListPrint[col][row] + " "

        print(rowString)


printTable(testTableData)
