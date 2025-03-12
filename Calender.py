# Getting the month and year
import calendar

def cal():
    try:
        month = int(input("Enter number of the month: "))
        year = int(input("Enter the year: "))
        print(calendar.month(year, month))
    except ValueError:
        print("Please enter a valid input...")

cal()
