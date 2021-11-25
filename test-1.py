from openpyxl import Workbook, workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = input("Give me 1st input: ")
sheet["B1"] = input("Give me second ipnut: ")

workbook.save(filename="1st_excel_frompy.xlsx")

