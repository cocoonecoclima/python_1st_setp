from openpyxl import Workbook, workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "HELLO"
sheet["B1"] = "THERE"

workbook.save(filename="1st_excel_frompy.xlsx")

