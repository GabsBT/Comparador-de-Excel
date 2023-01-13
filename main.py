import openpyxl

# Open the two Excel files
file1 = openpyxl.load_workbook("file1.xlsx")
file2 = openpyxl.load_workbook("file2.xlsx")

# Get the first sheet in each file
sheet1 = file1.active
sheet2 = file2.active

# Compare the contents of the sheets
for row1, row2 in zip(sheet1.rows, sheet2.rows):
    for cell1, cell2 in zip(row1, row2):
        if cell1.value != cell2.value:
            print(f"Discrepancy found: {cell1.value} != {cell2.value}")
