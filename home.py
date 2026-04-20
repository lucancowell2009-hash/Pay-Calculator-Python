reg_hours = float(input('Enter number of regular paid hours: '))
pay = float(input('Enter hourly pay ($): '))
breaks_check = input('Did you take any breaks? (yes/no): ')

if breaks_check.lower() == 'yes':
    breaks = float(input('Enter time taken for breaks (minutes): '))

else:
    breaks = 0

late_hours_check = input('Did you work late hours? (yes/no): ')
if late_hours_check.lower() == 'yes':
    late_hours = float(input('Enter number of late hours: '))

else:
    late_hours = 0

over_hours_check = input('Did you work overtime hours? (yes/no): ')
if over_hours_check.lower() == 'yes':
    over_hours = float(input('Enter number of overtime hours: '))

else:
    over_hours = 0    
    
weekend_check = input('Did you work on the weekend? (yes/no): ')
if weekend_check.lower() == 'yes':
    weekend_hours = float(input('Enter number of regular hours worked on the weekend: '))

else:
    weekend_hours = 0

total_pay = (reg_hours * pay) + (late_hours * pay * 1.5) + (over_hours * pay * 2) + (weekend_hours * pay * 2) - breaks * (pay / 60)
print('Total pay: $', total_pay)
