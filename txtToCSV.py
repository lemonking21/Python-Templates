################################################################################
# Created By Kyle Krug
# Created on 7/9/2019
# This was created to use as a template for conversions from TXT file to a CSV 
# file for easier use in a dataframe
# IMPORTANT!!!!
# This txt file must already have a form of a delimiter inorder for the
#conversion to progress correctly!!!
################################################################################
import csv
def slowdwn():
    print('..')
    print('....')
    print('......')
    
def choice():
    select=input("Options:\n-Enter 1 to convert csv to txt \n-Enter 2 to Convert txt to csv\n-Enter 3 to Exit")
    return select
def main():
    select = choice()
    txt_file =r"texttest.txt"
    csv_file =r"test.csv"
    if select == 1:
        in_csv = txt.reader(open(csv_file, "r"), delimiter = '\t')
        out_txt = txt.writer(open(txt_file, 'w'))
        out_txt.writerows(in_csv)
        slowdwn()
    elif select == 2:
        in_txt = csv.reader(open(txt_file, "r"), delimiter = '\t')
        out_csv = csv.writer(open(csv_file, 'w'))
        out_csv.writerows(in_txt)
        slowdwn()
    elif select == '3':
        quit()
    else:
        main()
main()

