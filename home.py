reg_hours = float(input('Enter number of regular paid hours: '))
pay = float(input('Enter hourly pay ($): '))
breaks_check = input('Did you take any breaks? (y/n): ')

if breaks_check.lower() == 'y':
    breaks = float(input('Enter time taken for breaks (minutes): '))

else:
    breaks = 0

late_hours_check = input('Did you work late hours? (y/n): ')
if late_hours_check.lower() == 'y':
    late_hours = float(input('Enter number of late hours: '))

else:
    late_hours = 0

over_hours_check = input('Did you work overtime hours? (y/n): ')
if over_hours_check.lower() == 'y':
    over_hours = float(input('Enter number of overtime hours: '))

else:
    over_hours = 0    
    
weekend_check = input('Did you work on the weekend? (y/n): ')
if weekend_check.lower() == 'y':
    weekend_hours = float(input('Enter number of regular hours worked on the weekend: '))

else:
    weekend_hours = 0

total_pay = (reg_hours * pay) + (late_hours * pay * 1.5) + (over_hours * pay * 2) + (weekend_hours * pay * 2) - breaks * (pay / 60)
print('Total pay: $', total_pay)

if total_pay > threshold:
    print('You are over the tax threshold.')
    taxable_income = total_pay - threshold
    tax_rate = 0.19
    tax_amount = taxable_income * tax_rate
else:
    print('You are under the tax threshold.')
    tax_amount = 0

net_pay = total_pay - tax_amount
print('Net pay after tax: $', net_pay)
