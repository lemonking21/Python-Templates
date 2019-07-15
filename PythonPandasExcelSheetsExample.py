################################################################################
# Created By Kyle Krug
# Created on 7/10/2019
# This was created to be used as a template on how to access teh different 
# sheets in an excel spread sheet file
#NOTES!!!! THIS CAN BE UPDATED TO WORK with a CSV file only
#need to swap read_excel with read_csv!!
################################################################################
import pandas
import xlrd

filename = r'C:\\Users\\kkrug\Documents\\ExcelTestfiles\\test sheets.xlsx'
wb = xlrd.open_workbook(filename, on_demand= True)
length= len(wb.sheet_names())
i= 0
list_num ={''}
for i in range (0,length):
    sheet = wb.sheet_by_index(i)
    col = sheet.ncols
    col =int(col)
    row = sheet.nrows
    row =int(row)
    ####################################################################issue reading rows in correctly, keeps adding newline
    for r in range(0,row):
       for c in range (0, col):
            list_num.append(sheet.cell_value(r,c))