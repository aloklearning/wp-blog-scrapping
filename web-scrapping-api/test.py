# For testing how this xlwt works
import xlwt
from xlwt import Workbook

# workbook is created
wb = Workbook()

# add_sheet is used to create sheet
data_sheet = wb.add_sheet("CL Blog Post Data")

style = xlwt.easyxf('font: bold 1') 
data_sheet.write(0, 0, 'BLOG TITLE', style) 
data_sheet.write(0, 1, 'BLOG URL', style) 
data_sheet.write(1, 0, 'ANOTHER DATA', style) 
wb.save('xlwt blog_data.xls')