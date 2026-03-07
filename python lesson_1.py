name='alex'
age=25
hourly_rate=15.5
is_employed=True
total_pay=hourly_rate*40
print(f"{name} earned ${total_pay} this week.")
if age>=18:
    print(f"{name} is an adult and is employed.")
else:
    print(f"{name} is either not an adult or not employed.")

hourly_worked=45
standard_rate=20
if hourly_worked<=40:
    total_pay=hourly_worked*standard_rate    
else:
    overtime_hours=hourly_worked-40
    total_pay=40*standard_rate+overtime_hours*standard_rate*1.5