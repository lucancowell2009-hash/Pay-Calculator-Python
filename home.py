
reg_hours = float(input('Enter number of regular paid hours: '))
pay = float(input('Enter hourly pay ($): '))
breaks_check = input('Did you take any breaks? (y/n): ')
threshold = 350

if breaks_check.lower() == 'y':
    breaks = float(input('Enter time taken for breaks (minutes): '))

else:
    breaks = 0

late_hours_check = input('Did you work late hours? (y/n): ')
if late_hours_check.lower() == 'y':
    late_hours = float(input('Enter number of late hours: '))
    late_custom = input('Use custom late rate instead of 1.5x? (y/n): ')
    if late_custom.lower() == 'y':
        late_multiplier = float(input('Enter custom late multiplier (e.g., 1.25): '))
        late_rate = pay * late_multiplier
    else:
        late_rate = pay * 1.5
else:
    late_hours = 0
    late_rate = 0

over_hours_check = input('Did you work overtime hours? (y/n): ')
if over_hours_check.lower() == 'y':
    over_hours = float(input('Enter number of overtime hours: '))
    over_custom = input('Use custom overtime rate instead of 2x? (y/n): ')
    if over_custom.lower() == 'y':
        over_multiplier = float(input('Enter custom overtime multiplier (e.g., 2.5): '))
        over_rate = pay * over_multiplier
    else:
        over_rate = pay * 2
else:
    over_hours = 0  
    over_rate = 0  
    
weekend_check = input('Did you work on the weekend? (y/n): ')
if weekend_check.lower() == 'y':
    weekend_hours = float(input('Enter number of regular hours worked on the weekend: '))
    weekend_custom = input('Use custom weekend rate instead of 2x? (y/n): ')
    if weekend_custom.lower() == 'y':
        weekend_multiplier = float(input('Enter custom weekend multiplier (e.g., 1.5): '))
        weekend_rate = pay * weekend_multiplier
    else:
        weekend_rate = pay * 2
else:
    weekend_hours = 0
    weekend_rate = 0


total_pay = (reg_hours * pay) + (late_hours * late_rate) + (over_hours * over_rate) + (weekend_hours * weekend_rate) - breaks * (pay / 60)
print(f'Total pay: $ {total_pay}')

if total_pay > threshold:
    print('You are over the tax threshold.')
    taxable_income = total_pay - threshold
    tax_rate = 0.16
    tax_amount = taxable_income * tax_rate
else:
    print('You are under the tax threshold.')
    tax_amount = 0

net_pay = total_pay - tax_amount
print(f'Net pay after tax: $', net_pay)
