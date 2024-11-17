"""
import os
Folder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/automate"
for file,file1 in enumerate(os.listdir(Folder_Path)):
    a= f"f_{file+1}.txt"
    os.rename(os.path.join(Folder_Path,file1), os.path.join(Folder_Path,a))
print("file renamed")
"""

import os
Folder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/Folder_nameChange"
NewFolder_Path="/Users/sumitasinha/PycharmProjects/pythonProject/codespaces-blank/automate"
os.rename(Folder_Path,NewFolder_Path)
print("file renamed")

