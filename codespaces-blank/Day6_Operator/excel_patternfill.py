from openpyxl import Workbook
from openpyxl.styles import PatternFill

work_book = Workbook()
work_sheet = work_book.active

work_sheet.append(["student_name", "Roll_No", "Marks", "Remarks"])

students_data = [
    {"student_name": "John Doe", "Roll_No": 101, "Marks": 45},
    {"student_name": "Jane Smith", "Roll_No": 102, "Marks": 29},
    {"student_name": "Sam Wilson", "Roll_No": 103, "Marks": 78},
    {"student_name": "Anna Brown", "Roll_No": 104, "Marks": 32},
]

for i,student in enumerate(students_data, start=2):
    name = student["student_name"]
    roll_no = student["Roll_No"]
    marks = student["Marks"]
    remarks = f'=IF(C{i}>=33,"Pass","Fail")'
    work_sheet.append([name, roll_no, marks, remarks])
    cell = work_sheet.cell(row=i, column=4)
    cell.value = remarks
    if marks <33:
        cell.fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
    else:
        cell.fill = PatternFill(start_color="008000", end_color="008000", fill_type="solid")


work_book.save("student_data4.xlsx")

print("Excel file 'student_data3.xlsx' has been created successfully.")