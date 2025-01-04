"""
import os
Folder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/automate"
for file,file1 in enumerate(os.listdir(Folder_Path)):
    a= f"f_{file+1}.txt"
    os.rename(os.path.join(Folder_Path,file1), os.path.join(Folder_Path,a))
print("file renamed")
"""
"""
#folder rename
import os
Folder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/Folder_nameChange"
NewFolder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/automate"
os.rename(Folder_Path,NewFolder_Path)
print("file renamed")

"""

import os
import openpyxl

path1= "//Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/Day6_Operator/para.txt"
path= "//Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/Day6_Operator/DBTables.xlsx"

workbook = openpyxl.load_workbook(path)
worksheet = workbook.active

with open(path1, 'a') as file:
    for row in worksheet.iter_rows():
        for cell in row:
            file.write(str(cell.value) + ',')
        file.write('\n')

print("Data extracted and added to the text file successfully!")






