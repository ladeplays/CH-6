# customer_sales_report.py - 
# program that reads the sales.csv file and creates 
# a new file with the customer ID and calculated total (as shown in salesreport.csv)

import csv

sales = open('sales.csv','r')
sales_report = open('sales_report.csv','r')
outfile = open('salesreport.csv', 'w')
csv_file = csv.reader(sales)
next(csv_file)

values={'250':0,
        '251':0,
        '252':0,
        '253':0,
        '254':0,
        '255':0,
        '256':0,
        '257':0,
        '258':0,
        '259':0,
        '260':0,
        '261':0}


def main():
    for i in csv_file:
        total = float(i[3])
        tax = float(i[4])
        freight = float(i[5])
        identification = (i[0])

        if identification in values:
            values[identification] = values[identification] + total + tax + freight
             #outfile.write(f'{values[identification]}\n')
    outfile.write(f'Customer ID,Total\n')
    for k,v in values.items():
        outfile.write(f'{k},{v:.2f}\n')
main()
outfile.close()
