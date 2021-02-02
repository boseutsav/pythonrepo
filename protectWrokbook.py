from openpyxl import load_workbook
from openpyxl.workbook.protection import WorkbookProtection

workbook = load_workbook("C:\\testtemp\\Jim.xlsx", read_only=False, keep_vba=True)
workbook.security = WorkbookProtection(workbookPassword = 'secret-password', lockStructure = True)
workbook.save("C:\\testtemp\\Harry.xlsx")