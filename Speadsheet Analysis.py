# Building a program to carryout basic data analysis on sales.csv file
import csv


with open('sales.csv', 'r') as csv_file:         # how to read the csv file
    spreadsheet = csv.DictReader(csv_file)

    line_count = 0
    monthly_sales = []
    monthly_expenses = []
    for row in spreadsheet:
        monthly_sales.append(row['sales'])
        monthly_expenses.append(row['expenditure'])
        # line_count += 1
    # Test if code works
    # print(monthly_sales)
    # print(monthly_expenses)
    monthly_sales_amount = [int(i) for i in monthly_sales]     # code to convert list strings to integers
    monthly_expense_bill = [int(i) for i in monthly_expenses]
    annual_sales = sum(monthly_sales_amount)

    annual_expenditure = sum(monthly_expense_bill)
    summary = f'\nYour annual sales for 2018 is ${annual_sales} though you spent around ${annual_expenditure}.'
    print(summary)

with open('todo.txt', 'a') as todo_file:
    # added = csv.DictWriter(csv_file, fieldnames=['sum'])
    todo_file.write(summary)


# Program to read summary of monthly sales and expense costs
with open('sales.csv', 'r') as csv_file:  # how to read the csv file
    summary_account = csv.DictReader(csv_file)

    for row in summary_account:
        while line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tIn {row["month"]} {row["year"]}, the department earned sales of ${row["sales"]} '
              f'and spent ${row["expenditure"]}.')
            line_count += 1
        # print(enter)


# print(f'went through {line_count} lines')
