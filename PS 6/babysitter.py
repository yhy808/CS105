#
# babysitter.py
#
# A program to compute the total time worked and the total amount earned by 
# the babysitter.
#
# Author: Hongyi Yu


rate = int(input('Enter the hourly rate in dollars: '))
start_time = input('Enter the start time: ')
end_time = input('Enter the end time: ')

components_start = start_time.split()
start_hour = int(components_start[0])
start_period = components_start[1]

components_end = end_time.split()
end_hour = int(components_end[0])
end_period = components_end[1]

if start_period == 'PM':
    start_hour += 12
if end_period == 'PM':
    end_hour += 12

worked_hours = end_hour - start_hour
earning = worked_hours * rate
print()
print('The babysitter worked', worked_hours, 'hours and earned', '$' + str(earning) + '.')
    