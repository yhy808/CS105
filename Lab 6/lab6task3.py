#
# lab6task3.py - converts a date string in the form
# month/day/year to one in the form day-month-year
#

date = input('Enter a date in the form month/day/year: ')

components = date.split('/')
month = components[0]
day = components[1]
year = components[-1]

new_components = [day, month, year]
new_date = '-'.join(new_components)
print('The reformatted date is:', new_date)
